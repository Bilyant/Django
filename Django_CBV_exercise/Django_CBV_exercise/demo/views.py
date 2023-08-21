from django.shortcuts import render
from Django_CBV_exercise.demo.models import Books
from django.views import generic as views
from django.urls import reverse_lazy
from django.forms import modelform_factory


def index(request):
    context = {
        'books': Books.objects.all()
    }
    return render(request, 'books/books-all.html', context)


# views.CreateView
# views.ListView
# views.DetailView
# views.UpdateView
# views.DeleteView

# the most basic CBV
class BooksListView(views.View):

    def get(self, *args, **kwargs):
        context = {
            'books': Books.objects.all()
        }
        return render(self.request, 'books/books-all.html', context)

    def post(self):
        pass


class BooksTemplateView(views.TemplateView):
    template_name = 'books/books-all.html'

    # static data
    extra_context = {
        'books': Books.objects.all(),
    }

    # dynamic data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.all()
        return context


class RedirectToHomeView(views.RedirectView):
    url = reverse_lazy('index')


# --------------------------------- GENERIC VIEWS -------------------------------


class BooksListGenericView(views.ListView):
    template_name = 'books/books-all-generic-view.html'
    model = Books
    paginate_by = 6

    # object_list == books_list (model name + '_list')
    # context_object_name = 'books'

    # def render_to_response(self, context, **response_kwargs):
    #     super().render_to_response(context, **response_kwargs)

    # Books.objects.filter(title__icontains='search')  -- if it were a fbv
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class BookDetailsView(views.DetailView):
    model = Books
    template_name = 'books/book-details.html'
    # pk_url_kwarg = 'id'


# --------------------------------- CRUD Views -------------------------------------------

# Forms:
# 1. Auto created (default)
# 2. form_class = "CustomCreatedForm" - return class
# 3. override get_form_class() - return instance
# 4. override get_form() - return instance

class DisableFormFieldsMixin:
    disabled_fields = ()

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for field in self.disabled_fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'

        return form


class BookCreateView(DisableFormFieldsMixin, views.CreateView):
    model = Books
    template_name = 'books/book-create.html'
    fields = '__all__'
    # form_class = CustomForm
    success_url = reverse_lazy('create view')
    disabled_fields = ('title',)


class BookUpdateView(views.UpdateView):
    models = Books
    template_name = 'books/book-update.html'


class BookDeleteView(DisableFormFieldsMixin, views.DeleteView):
    model = Books
    template_name = 'books/book-delete.html'
    success_url = reverse_lazy('list view')
    form_class = modelform_factory(
        model=Books,
        fields = '__all__',
    )
    disabled_fields = ('title', 'author')

    def get_form_kwargs(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)
        return form_kwargs
