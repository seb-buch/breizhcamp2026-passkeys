<script>
	import { Presentation } from '@slyd/core';

	import '@slyd/core/themes/default.css';
	import {
		AsymmetricCryptoSlide,
		AsymmetricEncryptionIllustration,
		AsymmetricSigningIllustration,
		SpongeBobTransitionSlide,
		TitleSlide,
		Who
	} from '$lib';
</script>

<svelte:head>
	<title>Passkeys - Sébastien Buchoux -BreizhCamp 2026</title>
	<script src="https://kit.fontawesome.com/b8d279694e.js" crossorigin="anonymous"></script>
</svelte:head>

<Presentation>
	<TitleSlide />
	<Who />
	<SpongeBobTransitionSlide />
	<AsymmetricCryptoSlide />
	<AsymmetricEncryptionIllustration />
	<AsymmetricSigningIllustration />
</Presentation>
