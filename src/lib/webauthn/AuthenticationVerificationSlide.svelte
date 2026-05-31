<script lang="ts">
	import snippetExample from './code/authentication-server.verify.py?raw';
	import AuthenticationCodeSlide from '$lib/webauthn/common/AuthenticationCodeSlide.svelte';

	const description = 'Vérification et authentification';
	const location = 'server';
	const rowID = 7;
	const colMove = '2-3';
	const highlightedLines = '3-6|8|11-36|12|13|14|15|17|19|3,21,29|22|23-25|26-27|28';
</script>

<AuthenticationCodeSlide
	codeSnippet={snippetExample}
	{description}
	{highlightedLines}
	{location}
	{rowID}
	{colMove}
/>
