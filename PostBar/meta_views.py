from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.views.generic import UpdateView, ListView, FormView, DetailView, CreateView


class ICreateView(CreateView, LoginRequiredMixin):
    template_name_suffix = '_Create'


class IUpdateView(UpdateView, LoginRequiredMixin):
    template_name_suffix = '_update'

    def dispatch(self, request, *args, **kwargs):
        return super(IUpdateView, self).dispatch(request, *args, **kwargs)


class IFormView(FormView):
    template_name_suffix = '_detail'


class IDetailView(DetailView):
    template_name_suffix = '_detail'


class IListView(ListView):
    template_name_suffix = '_list'
    filter_keys = []
    ordering = None

    def get_queryset(self):
        new_context = super().get_queryset()
        new_context: QuerySet = new_context.filter(**self.get_filter_kwargs())
        ordering = self.request.GET.get("ordering", None)
        self.ordering = ordering if ordering else self.ordering
        if self.ordering is not None:
            new_context = new_context.order_by(self.ordering)
            # new_context["ordering"]
        return new_context

    def get_filter_kwargs(self):
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
