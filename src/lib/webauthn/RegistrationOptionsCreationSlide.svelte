<script lang="ts">
	import snippetExample from './code/registration-server.create_options.py?raw';
	import RegistrationCodeSlide from '$lib/webauthn/common/RegistrationCodeSlide.svelte';

	const description = "Création des options d'enregistrement";
	const location = 'server';
	const rowID = 1;
	const colMove = '2-3';
	const highlightedLines = '1-4|6|9-13|1,14,25|15-16|17-19|20|21-24|9-25';
</script>

<RegistrationCodeSlide
	codeSnippet={snippetExample}
	{description}
	{highlightedLines}
	{location}
	{rowID}
	{colMove}
/>
