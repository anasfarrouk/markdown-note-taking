from    django.db   import  models
from    django.conf import  settings

# Create your models here.
def user_directory_path(instance,filename):
    return  "user_{0}/{1}".format(instance.user.id,filename)

class Note(models.Model):
    upload          =   models.FileField(upload_to=user_directory_path)
    owner           =   models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="uploads")
    date_created    =   models.DateTimeField(auto_now_add=True)

