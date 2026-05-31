<script lang="ts">
	import { Slide, SpeakerNotes } from '@seb-buch/slyd';

	import background from '$lib/assets/images/background-title.png';
</script>

<Slide backgroundImage={background} backgroundSize="cover">
	<div class="title-content">
		<h1>
			Passkeys :<br />
			Adieu les mots de passe, bonjour la sécurité sans friction !
		</h1>
		<p class="speaker">Sébastien Buchoux</p>
		<p class="event">BreizhCamp 2026</p>
	</div>
	<SpeakerNotes>
		<p>
			Bonjour à toutes et tous!<br />
			Je vous propose de passer la prochaine demi-heure à parler d'une méthode d'authentification que
			vous avez sans doute déjà vu apparaître sur certains des sites que vous fréquentez.<br />
			Il s'agit de l'authentification WebAuthn ou, pour simplifier, des passkeys.<br />
			On va voir ensemble quelles sont les différences avec l'authentification par mot de passe, les détails
			techniques, mais aussi comment on peut mettre en place ce type d'authentification avec une application
			qui nous servira d'exemple tout au long de cette session.
		</p>
	</SpeakerNotes>
</Slide>

<style>
	.title-content {
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: end;
		align-items: center;
		background: #f1f5f8bb;
		backdrop-filter: blur(10px);
		border-radius: 10px;
		padding: 20px;
		box-sizing: border-box;

		h1 {
			font-size: 2.5em;
			text-align: left;
		}

		.speaker {
			align-self: flex-end;
			font-size: 1.2em;
			font-weight: bold;
			letter-spacing: 0.03em;
			text-align: right;
			margin: 5em 0 0.2em;
		}

		.event {
			font-size: 0.8em;
			color: #ea7e14;
			margin: 5em 0 0;
			letter-spacing: 0.08em;
			text-align: right;
		}
	}
</style>
