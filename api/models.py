from    django.db   import  models
from    django.conf import  settings
from    .validators import  validate_markdown_file

# Create your models here.
def user_directory_path(instance,filename):
    return  "user_{0}/{1}".format(instance.owner.id,filename)

class Note(models.Model):
    upload          =   models.FileField(upload_to=user_directory_path,validators=[validate_markdown_file])
    owner           =   models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="uploads")
    date_created    =   models.DateTimeField(auto_now_add=True)

