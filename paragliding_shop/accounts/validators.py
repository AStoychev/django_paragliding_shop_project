from django.core import exceptions
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

ONLY_LETTERS_EXCEPTIONS_VALIDATOR = "Ensure this value contains only letters."


def validate_only_alphanumeric(value):
    for ch in value:
        if not ch.isalnum():
            raise exceptions.ValidationError(ONLY_LETTERS_EXCEPTIONS_VALIDATOR)


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f'Max file size is {self.max_size:.2f} MB'