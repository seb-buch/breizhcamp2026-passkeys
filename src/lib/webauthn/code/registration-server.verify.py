from webauthn import verify_registration_response
from webauthn.helpers.structs import RegistrationCredential

from myapp import RelyingParty, WebauthnCredential, User, PasskeyStorage


def verify_and_store_registration(
    registration: RegistrationCredential,
    expected_challenge: bytes,
    rp: RelyingParty,
    user: User,
    storage: PasskeyStorage
) -> None:
    validated = verify_registration_response(
        credential=registration,  # From client (created by authenticator from options)
        expected_challenge=expected_challenge,  # From created options
        expected_rp_id=rp.id,  # domain name (e.g. "krabsvault.com")
        expected_origin=rp.origin,
        require_user_verification=False,
    )  # May raise InvalidRegistrationResponse !

    passkey = WebauthnCredential.from_registration_and_user(registration=validated, user=user)

    storage.save_passkey(passkey)
