<script lang="ts">
	import { Slide, SpeakerNotes, VerticalSpacer } from '@seb-buch/slyd';
	import backgroundImage from '$lib/story/images/bob-nightmare.png';
</script>

<Slide {backgroundImage} backgroundSize="cover">
	<div class="victory-container fragment">
		<h3>Authentification par mots de passe</h3>
		<VerticalSpacer height="5em" />
		<p>Les faiblesses&nbsp;:</p>
		<ul>
			<li class="fragment">Vulnérabilité au phishing</li>
			<li class="fragment">Mots de passe faibles ou réutilisés</li>
			<li class="fragment">Secret partagé &equals; surface d'attaque double</li>
		</ul>
	</div>
	<SpeakerNotes>
		<p>TODO</p>
	</SpeakerNotes>
</Slide>

<style>
	.victory-container {
		height: 100%;
		width: 100%;
		background: #f1f5f8bb;
		backdrop-filter: blur(10px);
		border-radius: 10px;
		padding: 20px;
		box-sizing: border-box;

		p {
			text-align: center;
			font-size: 1.5em;
			font-weight: bold;
		}

		ul {
			list-style: none;
			text-align: center;
			font-size: 1.2em;

			li {
				line-height: 2;
			}
		}
	}
</style>
