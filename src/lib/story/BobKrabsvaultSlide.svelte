<script lang="ts">
	import { Slide, SpeakerNotes } from '@seb-buch/slyd';
	import scene from '$lib/story/images/bob_working.png';
	import emailNotification from '$lib/story/images/bob_email-notification.png';
	import bobKrabsvault from '$lib/story/images/bob_krabsvault.png';
	import { type Snippet } from 'svelte';

	type Props = {
		screen?: 'krabsvault' | 'email';
		securityLevel?: 'password' | 'mfa' | 'passkey';
		children?: Snippet;
		legend?: string;
	};

	const { screen = 'email', securityLevel = 'password', children, legend }: Props = $props();

	let loadingState: 'loading' | 'ready' | 'failed' = $state('loading');
	let screenElement: HTMLElement;

	// Every slide mounts at once (slyd registers them all during its Init phase),
	// so onMount would make all BobKrabsvault instances race to set the demo's
	// global security level. Instead, watch slyd's `current` class on our enclosing
	// slide and (re)configure the demo only when this slide is actually shown.
	$effect(() => {
		const slideElement = screenElement.closest('.slyd-slide');
		if (!slideElement) return;

		const activate = () => {
			if (!slideElement.classList.contains('current')) return;

			setSecurityLevel();
		};

		const observer = new MutationObserver(activate);
		observer.observe(slideElement, { attributes: true, attributeFilter: ['class'] });

		// Cover the case where this slide is already current (e.g. direct hash load).
		activate();

		return () => observer.disconnect();
	});

	async function setSecurityLevel() {
		try {
			const response = await fetch('https://krabsvault.com/api/security-level', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ level: securityLevel })
			});

			if (response.ok) {
				loadingState = 'ready';
			} else {
				loadingState = 'failed';
			}
		} catch (err) {
			console.error('Error updating security level:', err);
			loadingState = 'failed';
		}
	}

	function openKrabsvault() {
		const slideElement = screenElement.closest('.slyd-slide');
		if (!slideElement) {
			return;
		}

		const presentationElement = slideElement.closest('.slyd');
		if (!presentationElement) {
			console.error('No presentation!');
			return;
		}
		if (presentationElement.classList.contains('overview')) {
			return;
		}

		console.log('Opening krabsvault');
		window.open('https://krabsvault.com', 'krabsvault');
	}
</script>

<Slide>
	{#if loadingState === 'failed'}
		<div class="no-connection-warning">
			<i class="fa fa-exclamation-triangle"></i>
			Could not connect to demo app
		</div>
	{/if}
	<div bind:this={screenElement}>
		{#if screen === 'email'}
			<img class="scene" src={scene} alt="Bob devant l'ordinateur" />
			<img class="scene fragment" src={emailNotification} alt="Bob a reçu une notification" />
		{:else}
			<button onclick={openKrabsvault}>
				<img class="scene" src={bobKrabsvault} alt="Bob devant krabsvault" />
			</button>
		{/if}
	</div>

	{#if legend}
		<p class="animated-legend fadeInAuto">{legend}</p>
	{/if}

	<SpeakerNotes>
		{@render children?.()}
	</SpeakerNotes>
</Slide>

<style>
	.no-connection-warning {
		z-index: 10;
		position: absolute;
		right: 20px;
		top: 20px;
		background: #f9e45b;
		border-radius: 10px;
		padding: 10px 20px;
		color: #6d4e09;
		font-size: 24px;
	}

	.scene {
		position: absolute;
		inset: 0;
		width: 100%;
		height: 100%;
		object-fit: cover;
		z-index: 1;
	}

	button {
		cursor: pointer;
	}
</style>
