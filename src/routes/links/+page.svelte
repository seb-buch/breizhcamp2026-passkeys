<script lang="ts">
	import background from '$lib/assets/images/spongebob-transition-background.jpeg';

	import '$lib/assets/theme-breizhcamp.css';

	const links = [
		{
			label: 'Slides',
			icon: 'fa-display',
			url: 'https://seb-buch.github.io/breizhcamp2026-passkeys'
		},
		{
			label: 'Feedback',
			icon: 'fa-comments',
			url: 'https://openfeedback.io/SRRLTK2p7mBWUfvuRudl/2026-06-26/1171002'
		},
		{
			label: 'Repo démo (KrabsVault)',
			icon: 'fa-brands fa-github',
			url: "https://github.com/seb-buch/passkey-demo"
		},
		{
			label: 'Repo présentation',
			icon: 'fa-brands fa-github',
			url: 'https://github.com/seb-buch/breizhcamp2026-passkeys'
		}
	];
</script>

<svelte:head>
	<title>Passkeys – BreizhCamp 2026</title>
	<script src="https://kit.fontawesome.com/b8d279694e.js" crossorigin="anonymous"></script>
</svelte:head>

<div class="page" style="background-image: url({background})">
	<div class="header">
		<h1>Passkeys</h1>
		<p class="subtitle">BreizhCamp 2026 — Sébastien Buchoux</p>
	</div>

		<div class="grid">
			{#each links as link (link.label)}
				<a class="card" href={link.url} target="_blank" rel="external">
					<i class="fa {link.icon} icon"></i>
					<span>{link.label}</span>
				</a>
			{/each}
		</div>
</div>

<style>
	:global(body) {
		margin: 0;
		padding: 0;
		font-family: sans-serif;
		font-size: 1.1rem;
	}

	.page {
		min-height: 100vh;
		background-size: cover;
		background-position: center;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 1rem;

	}

	.header {
    background: #f1f5f8cc;
    backdrop-filter: blur(12px);
		border-radius: 16px;
		padding: 1rem;
		text-align: center;
		max-width: 90vw;
	h1 {
		margin: 0 0 0.25em;
    font-size: 5rem;
		color: #1b5e20;
	}

	.subtitle {
		color: #244b24;
    font-size: 1.5rem;
		opacity: 0.8;
	}
	}


	.grid {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 5vw;

	.card {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap:3vh 3vw;
		background: white;
		border-radius: 12px;
		padding: 3vh 3vw;
		text-decoration: none;
		color: #244b24;
		border: 4px solid transparent;
		transition: border-color 0.2s ease;
		text-align: center;

		.icon {
			font-size: calc(max(10vw, 5rem));
		}
	&:hover {
		border-color: #2e7d32;
	}

	}
	}




</style>
