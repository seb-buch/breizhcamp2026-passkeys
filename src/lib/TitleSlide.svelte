<script lang="ts">
	import { Slide, SpeakerNotes } from '@slyd/core';

	import background from '$lib/assets/images/title-background.jpg';
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
			Je vous propose de passer la prochaine demi-heure à parler d'une méthode d'authentification
			que
			vous avez sans doute déjà vu apparaître sur certains des sites que vous fréquentez.<br />
			Il s'agit de l'authentification WebAuthn ou, pour simplifier, des passkeys.<br />
			On va voir ensemble quelles sont les différences avec l'authentification par mot de passe, les
			détails
			techniques, mais aussi comment on peut mettre en place ce type d'authentification avec une
			application
			qui nous servira d'exemple tout au long de cette session.
		</p>
	</SpeakerNotes>
</Slide>

<style>
  h1 {
    font-size: 2.5em;
    text-align: left;
  }

  .speaker {
    font-size: 1.1em;
    margin: 0 0 0.2em;
    font-weight: 600;
    letter-spacing: 0.03em;
    text-align: right;
  }

  .event {
    font-size: 0.8em;
    color: #ea7e14;
    margin: 0;
    letter-spacing: 0.08em;
    text-align: right;
  }
</style>
