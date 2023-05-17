from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


def validate_password(value):
    # Check if the password contains at least one number
    if not any(char.isdigit() for char in value):
        raise ValidationError(
            _("The password must contain at least one number."), code="no_number"
        )

    # Check if the password contains at least one special character
    if not any(char in "!@#$%^&*()_+-=[]{}|\\:;\"'<>,.?/~`" for char in value):
        raise ValidationError(
            _("The password must contain at least one special character."),
            code="no_special_char",
        )

    # Check if the password contains at least one capital letter
    if not any(char.isupper() for char in value):
        raise ValidationError(
            _("The password must contain at least one capital letter."),
            code="no_capital_letter",
        )
