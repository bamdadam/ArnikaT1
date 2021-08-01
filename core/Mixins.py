from django.http import Http404
from rest_framework.generics import get_object_or_404

from core.exceptions import PageNotFound


class MultipleFieldLookupMixin:
    def get_object(self):
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:  # Ignore empty fields.
                filter[field] = self.kwargs[field]
                # print(filter[field])
        # obj = get_object_or_404(queryset, **filter)  # Lookup the object
        if not hasattr(queryset, 'get'):
            queryset__name = queryset.__name__ if isinstance(queryset, type) else queryset.__class__.__name__
            raise ValueError(
                "First argument to get_object_or_404() must be a Model, Manager, "
                "or QuerySet, not '%s'." % queryset__name
            )
        try:
            obj = queryset.get(**filter)
        except queryset.model.DoesNotExist:
            model_instance = queryset.model.__name__
            # raise Http404('No %s matches the given query.' % queryset.model._meta.object_name)
            raise PageNotFound(detail=f"No {model_instance} matches the given query.")
        self.check_object_permissions(self.request, obj)
        return obj
