from    .models         import  Note
from    rest_framework  import  serializers

class   NoteSerializer(serializers.ModelSerializer):
    class   Meta:
        model   =   Note
        fields  =   ['id','upload','owner','date_created']
        read_only_fields    =   ['id','owner','date_created']

class   NoteGETSerializer(serializers.ModelSerializer):
    filename        =   serializers.SerializerMethodField()
    owner_username  =   serializers.SerializerMethodField()

    class   Meta:
        model   =   Note
        fields  =   ['id','filename','owner_username','date_created']

    def get_filename(self,obj):
        return  obj.upload.name.split('/')[-1]  if  obj.upload  else    None

    def get_owner_username(self,obj):
        return  getattr(obj.owner,'username',None)

