from    django.core.exceptions  import  ValidationError

ALLOWED_EXT     =   {".md"}
ALLOWED_MIME    =   {"text/markdown", "text/plain"}
MAX_SIZE        =   2 * 1024 * 1024  # 2 MB

def validate_markdown_file(f):
    if f.size > MAX_SIZE:
        raise ValidationError("File too large (max 2 MB).")

    name = f.name.lower()
    if not any(name.endswith(ext) for ext in ALLOWED_EXT):
        raise ValidationError("Only .md files allowed.")

    chunk = f.read(4096)
    f.seek(0)
    try:
        text = chunk.decode("utf-8")
    except Exception:
        raise ValidationError("File must be UTF-8 text (not binary).")

    if "\x00" in text:
        raise ValidationError("Invalid file content.")

