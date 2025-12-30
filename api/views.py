from    django.shortcuts            import  render
from    rest_framework.generics     import  CreateAPIView,ListAPIView,RetrieveAPIView
from    rest_framework.permissions  import  IsAuthenticated
from    rest_framework.response      import  Response
from    .serializers                import  NoteSerializer,NoteGETSerializer
from    .models                     import  Note
from    markdown                    import  markdown

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

    def retrieve(self,request,*args,**kwargs):
        note    =   self.get_object()
        file    =   note.upload
        text    =   file.read().decode('utf-8')
        html    =   markdown(text)
        return  Response({'html':html})

