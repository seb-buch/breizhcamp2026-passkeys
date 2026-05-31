<script lang="ts">
	import snippetExample from './code/registration-client.create.ts?raw';
	import RegistrationCodeSlide from '$lib/webauthn/common/RegistrationCodeSlide.svelte';

	const description = 'Création de la passkey';
	const location = 'browser';
	const rowID = 2;
	const colMove = '3-2';
	const highlightedLines = '1|3-6|4|5|8-15|9|10|11-14|17-20|18|19';
</script>

<RegistrationCodeSlide
	codeSnippet={snippetExample}
	{description}
	{highlightedLines}
	{location}
	{rowID}
	{colMove}
/>
