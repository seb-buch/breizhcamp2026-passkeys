<script lang="ts">
	import { Slide, SpeakerNotes } from '@seb-buch/slyd';
	import backgroundImage from '$lib/story/images/bob-nightmare.png';
</script>

<Slide {backgroundImage} backgroundSize="cover">
	<div class="victory-container fragment">
		<h3>Authentification MFA</h3>
		<i class="fa-solid fa-triangle-exclamation"></i>
		<p>L'authentification multi-factorielle <em>seule</em> ne protège pas du phishing&nbsp;!</p>
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

		.fa-triangle-exclamation {
			margin-top: 250px;
			margin-bottom: 40px;
			font-size: 100px;
			margin-left: 50%;
			transform: translateX(-50%);
			color: #ea3b14;
		}

		p {
			text-align: center;
			font-size: 1.5em;
			font-weight: bold;
		}
	}
</style>
