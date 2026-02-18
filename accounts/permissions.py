from functools import wraps
from django.core.exceptions import PermissionDenied

def group_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if hasattr(request.user, 'role') and request.user.role in roles:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied("Insufficient permissions for this module (RBAC)")
        return _wrapped
    return decorator