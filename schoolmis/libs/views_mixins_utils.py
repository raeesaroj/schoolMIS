from django.core.exceptions import PermissionDenied


class QueryMixin(object):

    def get_queryset(self):
        return super().get_queryset().select_related()


class OwnerListMixin(object):
    """
    get the objects list created by current user
    """
    def get_queryset(self):
        qs = super(OwnerListMixin, self).get_queryset()
        return qs.filter(created_by=self.request.user)


class OwnerMixin(object):
    """
    not allowed to update, delete and see details of objects created by other user
    """
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.created_by != self.request.user:
            raise PermissionDenied
        return super(OwnerMixin, self).dispatch(request, *args, **kwargs)


class OwnerCreateMixin(object):
    """
    create objects by the current loggedIn users
    """
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
