from    django.shortcuts        import  render
from    rest_framework.generics import  CreateAPIView
from    rest_framework.permissions  import  IsAuthenticated
from    .serializers            import  NoteSerializer
from    .models                 import  Note

# Create your views here.
class   NoteView(CreateAPIView):
    queryset            =   Note.objects.all()
    serializer_class    =   NoteSerializer
    permission_class    =   [IsAuthenticated]
    def post(self,serializer):
        serializer.save(owner=self.request.user)
