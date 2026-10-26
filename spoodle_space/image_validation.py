"""The upload contract shared by posts, member photos and dog photos."""
from rest_framework import serializers

MAX_IMAGE_BYTES = 2 * 1024 * 1024
MAX_IMAGE_DIMENSION = 4096
IMAGE_HELP = 'Use a JPEG, PNG, WebP or GIF up to 2 MB and 4096 × 4096 pixels.'


class CommunityImageField(serializers.ImageField):
    default_error_messages = {
        'invalid_image': 'This image could not be read. ' + IMAGE_HELP,
        'invalid': 'Choose an image file. ' + IMAGE_HELP,
        'empty': 'This image file is empty. Choose another image.',
    }

    def to_internal_value(self, data):
        # Check bytes before asking Pillow to decode the image.
        if getattr(data, 'size', 0) > MAX_IMAGE_BYTES:
            raise serializers.ValidationError(
                'This image is larger than 2 MB. Choose a smaller image.',
                code='image_too_large',
            )
        image = super().to_internal_value(data)
        if image.image.format not in ('JPEG', 'PNG', 'WEBP', 'GIF'):
            raise serializers.ValidationError(IMAGE_HELP, code='image_format')
        if max(image.image.size) > MAX_IMAGE_DIMENSION:
            raise serializers.ValidationError(
                'This image exceeds 4096 pixels in width or height. '
                'Resize it to fit within 4096 × 4096 pixels.',
                code='image_dimensions',
            )
        return image
