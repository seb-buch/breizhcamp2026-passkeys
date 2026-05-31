export async function callBackend(
	path: string,
	payload: RegistrationResponseJSON | AuthenticationResponseJSON | undefined = undefined
): Promise<Response> {
	console.log(payload);
	return fetch(path);
}
