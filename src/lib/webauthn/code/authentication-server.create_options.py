from webauthn import generate_authentication_options
from webauthn.helpers.structs import PublicKeyCredentialRequestOptions, UserVerificationRequirement

from myapp import RelyingParty


def create_authentication_options(
    rp: RelyingParty,
) -> PublicKeyCredentialRequestOptions:
    return generate_authentication_options(
        rp_id=rp.id,
        user_verification=UserVerificationRequirement.PREFERRED,
    )
