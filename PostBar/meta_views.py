from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.views.generic import UpdateView, ListView, DetailView, CreateView, DeleteView


class ILoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class IDeleteView(ILoginRequiredMixin, DeleteView):
    """ in order to create user have login  """
    template_name_suffix = '_confirm_Delete'


class ICreateView(ILoginRequiredMixin, CreateView):
    """ in order to create user have login  """
    template_name_suffix = '_create'


class IUpdateView(ILoginRequiredMixin, UpdateView):
    """ in order to create user have login  """

    template_name_suffix = '_update'

    def dispatch(self, request, *args, **kwargs):
        return super(IUpdateView, self).dispatch(request, *args, **kwargs)


class IDetailView(DetailView):
    template_name_suffix = '_detail'


class IListView(ListView):
    template_name_suffix = '_list'
    filter_keys = []
    ordering = None

    def get_queryset(self):
        """add additional constraint on query data set
        first filter the data set
        """
        query_set = super().get_queryset()
        query_set: QuerySet = query_set.filter(**self.get_filter_kwargs())
        ordering = self.request.GET.get("ordering", None)
        self.ordering = ordering if ordering else self.ordering
        if self.ordering is not None:
            query_set = query_set.order_by(self.ordering)
        return query_set

    def get_filter_kwargs(self):
        """get argument that appear in filter_keys and filter"""
        kwargs = {}
        for key in self.filter_keys:
            value = self.request.GET.get(key, None)
            if value:
                kwargs.setdefault(key, value)
        return kwargs

    def get_context_data(self, **kwargs):
        """add filter keys back to context so you can get it from template"""
        context = super().get_context_data(**kwargs)
        for key in self.filter_keys:
            value = self.request.GET.get(key, None)
            if value:
                context.setdefault(key, value)
        ordering = self.request.GET.get("ordering", None)
        self.ordering = ordering if ordering else self.ordering
        context["ordering"] = self.ordering
        return context
