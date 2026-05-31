<script lang="ts">
	import snippetExample from './code/authentication-client.get.ts?raw';
	import AuthenticationCodeSlide from '$lib/webauthn/common/AuthenticationCodeSlide.svelte';

	const description = 'Récupération de la passkey';
	const location = 'browser';
	const rowID = 2;
	const colMove = '3-2';
	const highlightedLines = '1|3-6|4|5|8-15|9|11-14|17-20|17|18|19';
</script>

<AuthenticationCodeSlide
	codeSnippet={snippetExample}
	{description}
	{highlightedLines}
	{location}
	{rowID}
	{colMove}
/>
