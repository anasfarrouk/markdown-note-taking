from    django.shortcuts            import  render
from    rest_framework.generics     import  CreateAPIView,ListAPIView,RetrieveAPIView
from    rest_framework.permissions  import  IsAuthenticated
from    .serializers                import  NoteSerializer,NoteGETSerializer
from    .models                     import  Note

# Create your views here.
class   CreateNoteView(CreateAPIView):
    serializer_class    =   NoteSerializer
    permission_classes  =   [IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class   ListNoteView(ListAPIView):
    serializer_class    =   NoteGETSerializer
    permission_classes  =   [IsAuthenticated]

    def get_queryset(self):
        return  Note.objects.filter(owner=self.request.user)

class   RetrieveNoteView(RetrieveAPIView):
    serializer_class    =   NoteGETSerializer
    permission_classes  =   [IsAuthenticated]
    lookup_field        =   'pk'

    def get_queryset(self):
        return  Note.objects.filter(owner=self.request.user)

