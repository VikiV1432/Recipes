from django.core.exceptions import ValidationError
ALLOWED_IMAGEFIELD_EXTENSIONS = [
    "jpg", "jpeg",
    "png",
    "gif",
    "bmp", "dib",
    "webp",
    "tif", "tiff",
    "ico"
]
def validate_image(file):
    ext=file.name.split('.')[-1].lower()
    if ext not in ALLOWED_IMAGEFIELD_EXTENSIONS:
        raise ValidationError(f"Unsupported file with extension:{ext}")