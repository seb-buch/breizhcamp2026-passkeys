from typing import Any

from webauthn import verify_authentication_response
from webauthn.authentication.verify_authentication_response import VerifiedAuthentication
from webauthn.helpers import parse_authentication_credential_json
from webauthn.helpers.structs import AuthenticationCredential

from myapp import PasskeyStorage, WebauthnCredential, RelyingParty


def verify_authentication(
    credential_json: str | dict[str, Any],
    expected_challenge: bytes,
    storage: PasskeyStorage,
    rp: RelyingParty
) -> WebauthnCredential:
    client_passkey: AuthenticationCredential = parse_authentication_credential_json(credential_json)

    stored_passkey: WebauthnCredential = storage.get_passkey(client_passkey.raw_id)

    authentication: VerifiedAuthentication = verify_authentication_response(
        credential=client_passkey,
        expected_challenge=expected_challenge,
        expected_rp_id=rp.id,
        expected_origin=rp.origin,
        credential_public_key=stored_passkey.public_key,
        credential_current_sign_count=stored_passkey.signature_count,
        require_user_verification=False,
    )  # May raise InvalidAuthenticationResponse !

    storage.update_signature_count(
        passkey_id=stored_passkey.id,
        signature_count=authentication.new_sign_count,
    )

    return stored_passkey
