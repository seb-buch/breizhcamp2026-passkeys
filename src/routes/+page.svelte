<script>
	import { Presentation } from '@seb-buch/slyd';

	import '@seb-buch/slyd/themes/default.css';

	import {
		AsymmetricCryptoSlide,
		AsymmetricEncryptionIllustration,
		AsymmetricSigningIllustration,
		AuthenticationFlowSlide,
		BackendLibraries,
		BobKrabsvaultSlide,
		Fido2Slide,
		ImplementationRecap,
		MondayMorningSlide,
		PasskeysVsPasswords,
		PhishingEmailPasswordSlide,
		RegistrationFlowSlide,
		SectionTitleSlide,
		SpongeBobTransitionSlide,
		Thanks,
		TitleSlide,
		WhatIsPasskey
	} from '$lib';
	import NighmarePasswordSlide from '$lib/story/NighmarePasswordSlide.svelte';
	import PasswordNotWorkingSlide from '$lib/story/PasswordNotWorkingSlide.svelte';
	import NoPasswordAuthenticationSlide from '$lib/story/NoPasswordAuthenticationSlide.svelte';
	import NighmareMfaSlide from '$lib/story/NighmareMfaSlide.svelte';
	import GoodnightSlide from '$lib/story/GoodnightSlide.svelte';
	import MfaNotWorkingSlide from '$lib/story/MfaNotWorkingSlide.svelte';

	import '$lib/assets/theme-breizhcamp.css';
	import '$lib/assets/additional.css';

	import PasskeyTypes from '$lib/conclusion/PasskeyTypes.svelte';
	import RegistrationOptionsCreationSlide from '$lib/webauthn/RegistrationOptionsCreationSlide.svelte';
	import RegistrationPasskeyCreationSlide from '$lib/webauthn/RegistrationPasskeyCreationSlide.svelte';
	import RegistrationVerificationSlide from '$lib/webauthn/RegistrationVerificationSlide.svelte';
	import AuthenticationOptionsCreationSlide from '$lib/webauthn/AuthenticationOptionsCreationSlide.svelte';
	import AuthenticationPasskeyGetSlide from '$lib/webauthn/AuthenticationPasskeyGetSlide.svelte';
	import AuthenticationVerificationSlide from '$lib/webauthn/AuthenticationVerificationSlide.svelte';
	import PlanktonPhishingSlide from '$lib/story/PlanktonPhishingSlide.svelte';
	import PlanktonVictorySlide from '$lib/story/PlanktonVictorySlide.svelte';
	import PhishingEmailMFASlide from '$lib/story/PhishingEmailMFASlide.svelte';
	import PhishingEmailPasskeysSlide from '$lib/story/PhishingEmailPasskeysSlide.svelte';
</script>

<svelte:head>
	<title>Passkeys &ndash; Sébastien Buchoux &ndash; BreizhCamp 2026</title>
	<script src="https://kit.fontawesome.com/b8d279694e.js" crossorigin="anonymous"></script>
</svelte:head>

<Presentation>
	<TitleSlide />

	<SpongeBobTransitionSlide />

	<MondayMorningSlide legend="On est lundi, Bob est content ..." />

	<BobKrabsvaultSlide
		securityLevel="password"
		legend="Comme tous les matins, Bob veut vérifier la recette du pâté de crabe ..."
	>
		<p>
			Comme tous les matins, Bob doit se connecter sur krabsvault.<br />
			C'est l'application développée par Mr Krabs pour sécuriser la recette des patés de crabe.<br
			/>
			Car, oui, même si Bob passe ses journées à cuisiner des patés de crabe,<br />
			il se connecte à krabsvault pour relire la recette.<br />
			Un peu comme les pilotes d'avion avec leur checklist avant chaque vol.<br />
		</p>
	</BobKrabsvaultSlide>
	<PhishingEmailPasswordSlide />
	<PlanktonPhishingSlide />
	<PlanktonVictorySlide />
	<NighmarePasswordSlide />

	<PasswordNotWorkingSlide />

	<BobKrabsvaultSlide securityLevel="mfa" />
	<PhishingEmailMFASlide />
	<PlanktonPhishingSlide />
	<PlanktonVictorySlide />
	<NighmareMfaSlide />

	<MfaNotWorkingSlide />

	<NoPasswordAuthenticationSlide />

	<AsymmetricCryptoSlide />
	<AsymmetricEncryptionIllustration />
	<AsymmetricSigningIllustration />

	<SectionTitleSlide title="Authentification avec FIDO2" />
	<Fido2Slide />
	<WhatIsPasskey />

	<SectionTitleSlide title="1. Enregistrement d'une passkey" />
	<BobKrabsvaultSlide securityLevel="passkey" screen="krabsvault" />
	<RegistrationFlowSlide />
	<RegistrationOptionsCreationSlide />
	<RegistrationPasskeyCreationSlide />
	<RegistrationVerificationSlide />

	<SectionTitleSlide title="2. Authentification avec une passkey" />
	<BobKrabsvaultSlide securityLevel="passkey" screen="krabsvault" />
	<AuthenticationFlowSlide />
	<AuthenticationOptionsCreationSlide />
	<AuthenticationPasskeyGetSlide />
	<AuthenticationVerificationSlide />

	<MondayMorningSlide legend="On est lundi (vraiment !), Bob est content ..." />
	<BobKrabsvaultSlide securityLevel="passkey" />
	<PhishingEmailPasskeysSlide />
	<GoodnightSlide />

	<SectionTitleSlide title="Conclusion" />
	<ImplementationRecap />
	<BackendLibraries />
	<PasskeyTypes />
	<PasskeysVsPasswords />

	<Thanks />
</Presentation>
