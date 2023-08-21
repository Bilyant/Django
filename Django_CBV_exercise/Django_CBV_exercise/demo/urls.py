from django.urls import path
from Django_CBV_exercise.demo.views import index, BooksListView, BooksTemplateView, RedirectToHomeView, \
    BooksListGenericView, BookDetailsView, BookCreateView, BookDeleteView

urlpatterns = (
    path('', index, name='index'),
    path('cbv/', BooksListView.as_view(), name='cbv'),
    path('cbv/template-view/', BooksTemplateView.as_view(), name='template view'),
    path('reverse/', RedirectToHomeView.as_view(), name=' redirect view'),
    path('list-view/', BooksListGenericView.as_view(), name='list view'),
    path('detail-view/<int:pk>/', BookDetailsView.as_view(), name='detail view'),
    path('create-view/', BookCreateView.as_view(), name='create view'),
    path('delete-view/<int:pk>/', BookDeleteView.as_view(), name='delete view'),
)
