<script lang="ts">
	import { Slide, SpeakerNotes } from '@seb-buch/slyd';
	import backgroundImage from '$lib/story/images/password-not-working-part1.png';
	import reactionImage from '$lib/story/images/password-not-working-part2.png';

	const reactionStyle = `background: url(${reactionImage});`;
</script>

<Slide {backgroundImage} backgroundSize="cover">
	<div class="reaction fragment" data-fragment-index="1" style={reactionStyle}></div>
	<p class="bob speech-bubble">
		Mr Krabs ! J'ai fait un rêve horrible !<br />
		Mon mot de passe était piraté par Plankton !
	</p>
	<p class="krabs speech-bubble fragment" data-fragment-index="1">
		Pas de panique mon p'ti Bob !<br />
		Tu sais bien qu'on utilise la sécurité multi-facteur !
	</p>

	<SpeakerNotes>
		<p>TODO</p>
	</SpeakerNotes>
</Slide>

<style>
	.reaction {
		position: absolute;
		background-position: 20px 20px !important;
		background-size: auto 1080px !important;
		width: calc(100% + 20px);
		height: calc(100% + 20px);
		top: -20px;
		left: -20px;
	}

	.speech-bubble {
		padding: 20px;
		border-radius: 10px;
		background-color: rgba(255, 255, 255, 0.8);
		width: fit-content;
		position: absolute;
		font-family: 'Comic Sans MS', sans-serif;

		&.bob {
			bottom: 100px;
			left: 20px;

			&:before {
				transform: skewX(-20deg);
				content: '';
				position: absolute;
				top: -40px;
				right: 140px;
				border-width: 0 0 40px 40px;
				border-style: solid;
				border-color: transparent transparent rgba(255, 255, 255, 0.8) transparent;
			}
		}

		&.krabs {
			bottom: 197px;
			right: 60px;

			&:before {
				transform: skewX(-20deg);
				content: '';
				position: absolute;
				top: -40px;
				left: 335px;
				border-width: 0 0 40px 40px;
				border-style: solid;
				border-color: transparent transparent rgba(255, 255, 255, 0.8) transparent;
			}
		}
	}
</style>
