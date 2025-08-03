from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            app_name = view.queryset.model._meta.app_label
            model_name = view.queryset.model._meta.model_name
            action_name = self.get_action(request)
        except AttributeError:
            return False
        return request.user.has_perm(f'{app_name}.{action_name}_{model_name}')

    def get_action(self, request):
        method_action = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_action.get(request.method.upper(), '')
