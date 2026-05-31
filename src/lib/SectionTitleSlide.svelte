<script lang="ts">
	import type { Snippet } from 'svelte';
	import { Slide, SpeakerNotes } from '@seb-buch/slyd';
	import background from '$lib/assets/images/background-title.png';

	type Props = {
		title: string;
		children?: Snippet;
	};

	const { title, children }: Props = $props();
</script>

<Slide backgroundImage={background} backgroundSize="cover">
	<div class="section-title">
		<h2>{title}</h2>
	</div>
	{#if children}
		<SpeakerNotes>{@render children()}</SpeakerNotes>
	{/if}
</Slide>

<style>
	.section-title {
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		background: #f1f5f8bb;
		backdrop-filter: blur(10px);
		border-radius: 10px;
		padding: 20px;
		box-sizing: border-box;
	}
</style>
