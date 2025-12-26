from    .models         import  Note
from    rest_framework  import  serializers

class   NoteSerializer(serializers.ModelSerializer):
    class   Meta:
        model   =   Note
        fields  =   ['id','upload','owner','date_created']
        read_only_fields    =   ['id','owner','date_created']
