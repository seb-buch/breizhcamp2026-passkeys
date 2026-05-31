<script>
	import CryptoKey from './common/CryptoKey.svelte';
	import { Slide, SpeakerNotes, VerticalSpacer } from '@seb-buch/slyd';

	const keySize = '150px';
</script>

<Slide>
	<h3>Cryptographie asymétrique</h3>

	<VerticalSpacer height="2em" />

	<div class="victory-container">
		<p>Une paire de clés liées:</p>

		<CryptoKey type="pair" size={keySize} orientation="vertical" />

		<div class="moustache fragment" data-fragment-index="1">
			<div></div>
			<div></div>
		</div>
		<div class="key-container">
			<div class="key-presentation fragment" data-fragment-index="2">
				<CryptoKey type="private" size={keySize} />
				<p class="key-type">Clé privée</p>
				<p class="key-description fragment" data-fragment-index="3">Secrète et non partagée</p>
			</div>
			<div class="key-presentation fragment" data-fragment-index="4">
				<CryptoKey type="public" size={keySize} />
				<p class="key-type">Clé publique</p>
				<p class="key-description fragment" data-fragment-index="5">Partagée publiquement</p>
			</div>
		</div>
	</div>
	<SpeakerNotes>
		<p>
			Pour s'authentifier sans mot de passe, une des piste est d'utiliser la cryptographie
			asymètrique qui repose sur une paire de clés:<br />
			une clé privée qui reste absolument secrète et qu'on ne partage sous aucun prétexte avec personne.<br
			/>
			Et une clé publique qui, elle, peut, et même, doit être partagée publiquement.<br />
			On ne va pas rentrer dans des détails cryptographiques ici, car ce n'est pas le sujet ici (et je
			n'ai de toute façon pas les compétences pour le faire).<br />
			En revanche, je vous propose de voir comment ça fonctionne en pratique.
		</p>
	</SpeakerNotes>
</Slide>

<style>
	.victory-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;

		.key-container {
			display: flex;
			flex-direction: row;
			justify-content: space-between;
			align-items: center;
			margin-top: 20px;

			width: 1200px;

			.key-presentation {
				display: flex;
				flex-direction: column;
				justify-content: center;
				align-items: center;

				p.key-type {
					margin-top: 1em;
					font-weight: bold;
					font-size: 1.2em;
				}

				p.key-description {
					font-size: 1em;
					text-align: center;
				}
			}
		}

		.moustache {
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
			padding: 0.5em 0;

			--height: 30px;
			--width: 800px;
			--line-color: #17395c;

			div {
				border: var(--line-color) 5px solid;
			}

			div:first-child {
				width: 5px;
				border: none;
				background: var(--line-color);
				height: var(--height);
			}

			div:nth-child(2) {
				width: var(--width);
				height: var(--height);
				background: none;
				border-bottom: none;
			}
		}
	}
</style>
