import { callBackend } from './myapp';

async function fetchRegistrationOptions(): Promise<PublicKeyCredentialCreationOptions> {
	const resp: Response = await callBackend('/webauthn/register/options');
	return PublicKeyCredential.parseCreationOptionsFromJSON(await resp.json()); // Baseline 2025
}

async function createPasskey(
	options: PublicKeyCredentialCreationOptions
): Promise<PublicKeyCredential> {
	// @ts-expect-error - https://github.com/microsoft/TypeScript/issues/60641
	return await navigator.credentials.create({
		publicKey: options
	}); // Baseline 2021
}

async function verifyRegistration(credential: PublicKeyCredential): Promise<Response> {
	const serialized = credential.toJSON(); // Baseline 2025
	return callBackend('/webauthn/register/options', serialized);
}
