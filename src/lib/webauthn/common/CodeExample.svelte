<script lang="ts">
	import { Code } from '@seb-buch/slyd';
	import type { Snippet } from 'svelte';

	type CodeProps = {
		children: Snippet;
		highlightedLines?: string;
		location?: 'server' | 'browser';
		description?: string;
	};

	const {
		children,
		location = 'server',
		highlightedLines = '',
		description = 'Passkey'
	}: CodeProps = $props();
</script>

<div class="code-container fragment">
	<div class="victory-container">
		<p>
			{description}
			&ndash;
			{location === 'server' ? 'Serveur' : 'Navigateur'}
			&ndash;
			{#if location === 'server'}
				Python <i class="fa-brands fa-python"></i>
			{:else}
				Typescript <i class="fa-brands fa-typescript"></i>
			{/if}
		</p>
		<Code
			{highlightedLines}
			lang={location === 'server' ? 'py' : 'ts'}
			theme="github-light-high-contrast"
			showLineNumbers
		>
			{@render children()}
		</Code>
	</div>
</div>

<style>
	.code-container {
		position: absolute;
		top: 0;
		height: 100%;
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;

		background: rgba(255, 255, 255, 0.7);
		backdrop-filter: blur(5px);
		z-index: 1;

		.victory-container {
			background: var(--slyd-slide-bg-color);
			padding: 1rem;
			border-radius: 0.5rem;
			box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);

			p {
				margin-bottom: 0;
			}
		}
	}
</style>
