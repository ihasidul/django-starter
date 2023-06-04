import magic
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible
from rest_framework.serializers import ValidationError


@deconstructible
class FileValidator(object):
    """
    Validator for files, checking the size, extension and mimetype.
    Usage::
    Using in model field:

        MyModel(models.Model):
            myfile = FileField(
                validators=[FileValidator(
                    max_size=1024 * 100,
                    content_types=('application/pdf', 'image/jpeg', 'image/png')
            )])

    Using in serializer field:

        MySerializer(serializers.Serializer):
            myfile = FileField(
                validators=[FileValidator(
                    max_size=1024 * 100,
                    content_types=('application/pdf', 'image/jpeg', 'image/png')
                )])
    """

    error_messages = {
        "max_size": (
            "Ensure this file size is not greater than %(max_size)s."
            " Your file size is %(size)s."
        ),
        "min_size": (
            "Ensure this file size is not less than %(min_size)s. "
            "Your file size is %(size)s."
        ),
        "content_type": (
            "Files of type %(content_type)s are not supported."
            "Please upload %(valid_file)s type file."
        ),
    }

    def __init__(self, max_size=None, min_size=None, content_types=()):
        self.max_size = max_size
        self.min_size = min_size
        self.content_types = content_types

    def __call__(self, data):
        if self.max_size is not None and data.size > self.max_size:
            params = {
                "max_size": filesizeformat(self.max_size),
                "size": filesizeformat(data.size),
            }
            raise ValidationError(
                self.error_messages["max_size"]
                .replace("%(max_size)s", params["max_size"])
                .replace("%(size)s", params["size"])
            )

        if self.min_size is not None and data.size < self.min_size:
            params = {
                "min_size": filesizeformat(self.min_size),
                "size": filesizeformat(data.size),
            }
            raise ValidationError(
                self.error_messages["min_size"].replace(
                    "%(min_size)s",
                    params["min_size"].replace("%(size)s", params["size"]),
                )
            )

        if self.content_types:
            content_type = magic.from_buffer(data.read(), mime=True)
            data.seek(0)
            accepted_type = ", ".join(self.content_types)
            if content_type not in self.content_types:
                params = {"content_type": content_type}
                raise ValidationError(
                    self.error_messages["content_type"]
                    .replace("%(content_type)s", params["content_type"])
                    .replace("%(valid_file)s", accepted_type)
                )

    def __eq__(self, other):
        return (
            isinstance(other, FileValidator)
            and self.max_size == other.max_size
            and self.min_size == other.min_size
            and self.content_types == other.content_types
        )
