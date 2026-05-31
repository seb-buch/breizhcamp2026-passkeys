<script lang="ts">
	import background from '$lib/assets/images/spongebob-transition-background.jpeg';

	import '$lib/assets/theme-breizhcamp.css';

	// TODO: fill in once repos are public and slides are deployed
	const TODO = 'https://github.com/seb-buch';

	const links = [
		{
			label: 'Slides',
			icon: 'fa-display',
			url: TODO
		},
		{
			label: 'Repo présentation',
			icon: 'fa-brands fa-github',
			url: TODO
		},
		{
			label: 'Repo démo (KrabsVault)',
			icon: 'fa-brands fa-github',
			url: "https://github.com/seb-buch/passkey-demo"
		},
		{
			label: 'Feedback',
			icon: 'fa-comments',
			url: 'https://openfeedback.io/SRRLTK2p7mBWUfvuRudl/2026-06-26/1171002'
		}
	];
</script>

<svelte:head>
	<title>Passkeys – BreizhCamp 2026</title>
	<script src="https://kit.fontawesome.com/b8d279694e.js" crossorigin="anonymous"></script>
</svelte:head>

<div class="page" style="background-image: url({background})">
	<div class="panel">
		<h1>Passkeys</h1>
		<p class="subtitle">BreizhCamp 2026 — Sébastien Buchoux</p>

		<div class="grid">
			{#each links as link (link.label)}
				<a class="card" href={link.url} target="_blank" rel="external">
					<i class="fa {link.icon} icon"></i>
					<span>{link.label}</span>
				</a>
			{/each}
		</div>
	</div>
</div>

<style>
	:global(body) {
		margin: 0;
		padding: 0;
		font-family: sans-serif;
		font-size: 30px;
	}

	.page {
		min-height: 100vh;
		background-size: cover;
		background-position: center;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.panel {
		background: #f1f5f8cc;
		backdrop-filter: blur(12px);
		border-radius: 16px;
		padding: 2.5rem 3rem;
		text-align: center;
		max-width: 900px;
		width: 90vw;
	}

	h1 {
		margin: 0 0 0.25em;
		font-size: 1.5em;
		color: #1b5e20;
	}

	.subtitle {
		margin: 0 0 2em;
		color: #244b24;
		font-size: 1em;
		opacity: 0.8;
	}

	.grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 1.5rem;
	}

	.card {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.75rem;
		background: white;
		border-radius: 12px;
		padding: 1.25rem;
		text-decoration: none;
		color: #244b24;
		border: 4px solid transparent;
		transition: border-color 0.2s ease;

		.icon {
			font-size: 8rem;
		}
	}

	.card:hover {
		border-color: #2e7d32;
	}

	.card-label {
		margin: 0;
		font-size: 0.9rem;
		font-weight: bold;
		display: flex;
		align-items: center;
		gap: 0.4rem;
	}
</style>
