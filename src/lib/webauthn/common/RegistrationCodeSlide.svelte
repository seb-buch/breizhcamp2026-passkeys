<script lang="ts">
	import browserIcon from '$lib/webauthn/common/images/browser.png';
	import authenticator from '$lib/webauthn/common/images/authenticator.png';
	import serverIcon from '$lib/webauthn/common/images/server.png';
	import { Slide, SpeakerNotes, VerticalSpacer } from '@seb-buch/slyd';
	import FlowDiagram from '$lib/webauthn/common/FlowDiagram.svelte';
	import './pointer.css';
	import CodeExample from '$lib/webauthn/common/CodeExample.svelte';
	import type { Snippet } from 'svelte';

	const streamLines = [
		{
			iconPath: authenticator,
			name: 'Authenticator'
		},
		{
			iconPath: browserIcon,
			name: 'Client'
		},
		{
			iconPath: serverIcon,
			name: 'Relying Party'
		}
	];

	const steps = [
		{ from: 1, to: 2, label: "Options d'enregistrement ?" },
		{ from: 2, to: 1, label: 'Challenge + options' },
		{ location: 1, label: 'navigator.credentials.create()' },
		{ from: 1, to: 0, label: 'Demande de création' },
		{ location: 0, label: 'Génération paire de clés + passkey' },
		{ from: 0, to: 1, label: 'Clé publique + ID passkey + ...' },
		{ from: 1, to: 2, label: 'Clé publique + ID passkey + ...' },
		{ location: 2, label: 'Vérif. challenge + enreg. passkey' },
		{ from: 2, to: 1, label: '✔ Enregistrement réussi' }
	];

	type Props = {
		codeSnippet: string;
		speakerNotes?: Snippet;
		highlightedLines?: string;
		description?: string;
		location?: 'server' | 'browser';
		rowID?: number;
		colMove?: '2-3' | '3-2';
	};

	const {
		codeSnippet,
		speakerNotes,
		highlightedLines = '',
		description = '',
		location = 'server',
		rowID = 1,
		colMove = '2-3'
	}: Props = $props();

	const flowDiagram = {
		// eslint-disable-next-line svelte/no-unused-svelte-ignore
		// svelte-ignore state_referenced_locally
		id: `registration-flow-creation-${rowID}-${colMove}`,
		// eslint-disable-next-line svelte/no-unused-svelte-ignore
		// svelte-ignore state_referenced_locally
		title: description,
		streamLines: streamLines,
		steps: steps
	};
</script>

<Slide>
	<h3>Cérémonie d'enregistrement</h3>

	<VerticalSpacer height="1em" />

	<div class="flow-diagram-container">
		<FlowDiagram useFragment={false} {flowDiagram} diagramStyle={{ stepHeight: 38 }} />
		<div class="fragment custom pointer row-{rowID} col{colMove}">
			<i class="fa fa-2x fa-location-dot"></i>
		</div>
	</div>
	<CodeExample {highlightedLines} {description} {location}>
		{codeSnippet}
	</CodeExample>
	{#if speakerNotes}
		<SpeakerNotes>
			{@render speakerNotes()}
		</SpeakerNotes>
	{/if}
</Slide>

<style>
	.flow-diagram-container {
		position: relative;
	}
</style>
