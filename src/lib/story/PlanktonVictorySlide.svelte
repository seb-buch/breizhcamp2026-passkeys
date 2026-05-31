<script lang="ts">
	import { Slide, SpeakerNotes } from '@seb-buch/slyd';
	import backgroundImage from '$lib/story/images/plankton-victory.png';
</script>

<Slide {backgroundImage} backgroundSize="cover">
	<div class="victory-container fragment custom">
		<p>You've been pwned</p>
	</div>
	<SpeakerNotes>
		<p>TODO</p>
	</SpeakerNotes>
</Slide>

<style>
	.victory-container {
		margin-top: 20%;

		backdrop-filter: brightness(20%);

		box-sizing: border-box;

		opacity: 0;
		transition: opacity 3s !important;

		p {
			text-align: center;
			font-size: 3.5em;
			font-weight: 200;
			word-spacing: 0.2em;
			font-family: 'Droid Serif', serif;
			color: crimson;
			text-transform: uppercase;
			line-height: 1.5;
		}
	}
</style>
