// place files you want to import through the `$lib` alias in this folder.
export { default as TitleSlide } from './TitleSlide.svelte';
export {
	AsymmetricCryptoSlide,
	AsymmetricEncryptionIllustration,
	AsymmetricSigningIllustration
} from './cryptography/';
export { default as Who } from './Who.svelte';
export { default as SpongeBobTransitionSlide } from './SpongeBobTransitionSlide.svelte';
export { default as SectionTitleSlide } from './SectionTitleSlide.svelte';
export { default as Fido2Slide } from './webauthn/Fido2Slide.svelte';
export { default as WhatIsPasskey } from './webauthn/WhatIsPasskey.svelte';
export { default as RegistrationFlowSlide } from './webauthn/RegistrationFlowSlide.svelte';
export { default as AuthenticationFlowSlide } from './webauthn/AuthenticationFlowSlide.svelte';
export { default as ImplementationRecap } from './conclusion/ImplementationRecap.svelte';
export { default as BackendLibraries } from './conclusion/BackendLibraries.svelte';
export { default as PasskeysVsPasswords } from './conclusion/PasskeysVsPasswords.svelte';
export { default as Thanks } from './conclusion/Thanks.svelte';
export { MondayMorningSlide, BobKrabsvaultSlide, PhishingEmailPasswordSlide } from './story/';
