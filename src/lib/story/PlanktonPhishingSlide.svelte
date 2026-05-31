<script lang="ts">
	import { Slide, SpeakerNotes } from '@seb-buch/slyd';
	import scene from '$lib/story/images/plankton-phishing_mask.png';
	import { type Snippet } from 'svelte';

	type Props = {
		url?: string;
		title?: string;
		loadTimeoutMs?: number;
		children?: Snippet;
		legend?: string;
	};

	const {
		url = 'https://krabsvau1t.com/stolen',
		title = 'Krabs Vault Phishing',
		loadTimeoutMs = 10,
		children,
		legend
	}: Props = $props();

	let loadingState: 'loading' | 'ready' | 'failed' = $state('loading');
	let timeout: ReturnType<typeof setTimeout> | undefined = $state();
	let regionEl: HTMLElement;

	// Every slide mounts at once (slyd registers them all during its Init phase),
	// so onMount would make all BobKrabsvault instances race to set the demo's
	// global security level. Instead, watch slyd's `current` class on our enclosing
	// slide and (re)configure the demo only when this slide is actually shown.
	$effect(() => {
		const slideEl = regionEl.closest('.slyd-slide');
		if (!slideEl) return;

		const activate = () => {
			if (!slideEl.classList.contains('current')) return;

			if (timeout) clearTimeout(timeout);
			loadingState = 'loading';
			timeout = setTimeout(() => {
				loadingState = 'ready';
			}, loadTimeoutMs);
		};

		const observer = new MutationObserver(activate);
		observer.observe(slideEl, { attributes: true, attributeFilter: ['class'] });

		// Cover the case where this slide is already current (e.g. direct hash load).
		activate();

		return () => observer.disconnect();
	});
</script>

<Slide>
	<div
		class="screen-region"
		bind:this={regionEl}
		role="button"
		tabindex="0"
		aria-label="Ouvrir {title} dans un nouvel onglet"
	>
		{#if loadingState !== 'ready'}
			<div class="fallback">
				{#if loadingState === 'loading'}
					<p>Loading...</p>
				{:else}<p class="failed">Failed !</p>
				{/if}
			</div>
		{:else}
			<iframe class="screen" src={url} {title} tabindex="-1" loading="lazy"></iframe>
		{/if}
	</div>

	<img class="scene" src={scene} alt="Plankton devant l'ordinateur" />

	{#if legend}
		<p class="animated-legend fadeInAuto">{legend}</p>
	{/if}

	<SpeakerNotes>
		{@render children?.()}
	</SpeakerNotes>
</Slide>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Titan+One&display=swap');

	.scene {
		position: absolute;
		inset: 0;
		width: 100%;
		height: 100%;
		object-fit: cover;
		pointer-events: none;
	}

	/* Slightly larger than the screen hole (slyd's 1920x1080 slide space) so the
		 iframe fully covers it. Edges are masked by the artwork, so this is approximate. */
	.screen-region {
		position: absolute;
		top: 30px;
		left: 330px;
		width: 1250px;
		height: 830px;
		background: #080808;
		overflow: hidden;
		cursor: pointer;
		z-index: 0;
	}

	.fallback,
	.screen {
		position: absolute;
		inset: 0;
		width: 100%;
		height: 100%;
		border: 0;
		object-fit: cover;
	}

	.fallback {
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 128px;
		font-family: 'Titan One', sans-serif;
		padding-top: 100px;
		background: #4a90d9;

		& .failed {
			color: #920000;
		}
	}
</style>
