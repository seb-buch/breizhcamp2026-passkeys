from webauthn import generate_registration_options
from webauthn.helpers.structs import PublicKeyCredentialCreationOptions, \
    PublicKeyCredentialDescriptor, AuthenticatorSelectionCriteria, \
    ResidentKeyRequirement, UserVerificationRequirement

from myapp import RelyingParty, User


def create_registration_options(
    rp: RelyingParty,
    user: User,
    existing_credentials: list[PublicKeyCredentialDescriptor],
) -> PublicKeyCredentialCreationOptions:
    return generate_registration_options(
        rp_id=rp.id,  # domain name (e.g. "krabsvault.com")
        rp_name=rp.name,  # human-readable name
        user_name=user.username,
        user_id=user.user_handle,  # random opaque identifier for ceremony
        user_display_name=user.display_name,
        exclude_credentials=existing_credentials,  # No creation if passkey exists
        authenticator_selection=AuthenticatorSelectionCriteria(
            resident_key=ResidentKeyRequirement.REQUIRED,  # Stored in authenticator
            user_verification=UserVerificationRequirement.PREFERRED,  # Loose user verification
        ),
    )
