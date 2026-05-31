<script lang="ts">
	import { Slide, SpeakerNotes } from '@seb-buch/slyd';
	import backgroundImage from '$lib/story/images/email-phishing.png';
</script>

<Slide {backgroundImage} backgroundSize="cover">
	<div class="phishing-container">
		<p class="from">Mr Krabs</p>
		<p class="to">Bob</p>
		<p class="subject">krabsvault</p>
		<div class="message">
			<p>Bonjour Bob,</p>
			<p>Plankton est très très intelligent !</p>
			<p>
				Vérifie bien ton mot de passe pour te connecter à <a
					href="https://krabsvau1t.com"
					target="phishing-login">https://krabsvault.com</a
				>.
			</p>
			<p>Mr Krabs</p>
		</div>
	</div>
	<SpeakerNotes>
		<p>
			Mais ce matin, Bob reçoit un email de Mr Krabs à propos de krabsvault.<br />
			Il s'agit d'une nouvelle fonctionnalité qui permet de sécuriser les patés de crabe.<br />
			Bob est curieux et décide de cliquer sur le lien pour en savoir plus.
		</p>
	</SpeakerNotes>
</Slide>

<style>
	.phishing-container {
		position: relative;
		height: 100%;
		width: 100%;
		font-size: 36px;

		.from {
			position: absolute;
			top: 327px;
			left: 792px;
		}

		.to {
			position: absolute;
			top: 390px;
			left: 792px;
		}

		.subject {
			position: absolute;
			top: 450px;
			left: 792px;
		}

		.message {
			position: absolute;
			top: 530px;
			left: 640px;
			font-size: 32px;

			width: 850px;
			height: 340px;
			overflow: hidden;

			p {
				margin-bottom: 0.2em;
			}

			a {
				text-decoration: underline;
			}
		}
	}
</style>
