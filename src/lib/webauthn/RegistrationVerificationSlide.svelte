<script lang="ts">
	import snippetExample from './code/registration-server.verify.py?raw';
	import RegistrationCodeSlide from '$lib/webauthn/common/RegistrationCodeSlide.svelte';

	const description = 'Vérification et stockage de la passkey';
	const location = 'server';
	const rowID = 7;
	const colMove = '2-3';
	const highlightedLines = '1-2|4|7-24|8-12|1,14,20|15|16-19|22-24';
</script>

<RegistrationCodeSlide
	codeSnippet={snippetExample}
	{description}
	{highlightedLines}
	{location}
	{rowID}
	{colMove}
/>
