import { callBackend } from './myapp';

async function fetchAuthenticationOptions(): Promise<PublicKeyCredentialRequestOptions> {
	const resp: Response = await callBackend('/webauthn/login/options');
	return PublicKeyCredential.parseRequestOptionsFromJSON(await resp.json()); // Baseline 2025
}

async function getPasskey(
	options: PublicKeyCredentialRequestOptions
): Promise<PublicKeyCredential> {
	// @ts-expect-error - https://github.com/microsoft/TypeScript/issues/60641
	return await navigator.credentials.get({
		publicKey: options
	}); // Baseline 2021
}

async function verifyRegistration(credential: PublicKeyCredential): Promise<Response> {
	const serialized = credential.toJSON(); // Baseline 2025
	return await callBackend('/webauthn/authenticate/options', serialized);
}
