<script lang="ts">
	import snippetExample from './code/authentication-server.create_options.py?raw';
	import AuthenticationCodeSlide from '$lib/webauthn/common/AuthenticationCodeSlide.svelte';

	const description = "Création des options d'authentification";
	const location = 'server';
	const rowID = 1;
	const colMove = '2-3';
	const highlightedLines = '1-2|4|7-13|8|1,10,13|11|12';
</script>

<AuthenticationCodeSlide
	codeSnippet={snippetExample}
	{description}
	{highlightedLines}
	{location}
	{rowID}
	{colMove}
/>
