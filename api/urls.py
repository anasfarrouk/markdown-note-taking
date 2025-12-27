from    django.urls     import  include,path
from    .views          import  CreateNoteView,ListNoteView,RetrieveNoteView

urlpatterns =   [
        path('upload/',CreateNoteView.as_view(),name='upload_note'),
        path('list/',ListNoteView.as_view(),name='list_notes'),
        path('note/<int:pk>/',RetrieveNoteView.as_view(),name='note-detail'),
        ]

