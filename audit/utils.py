from .models import AuditLog

def log_action(request, action, model, object_id, before='', after=''):
    ip = ''
    if hasattr(request, 'META'):
        ip = request.META.get('REMOTE_ADDR','')
    AuditLog.objects.create(
        action=action,
        model=model,
        object_id=object_id,
        user=getattr(request,'user',None) if hasattr(request,'user') else None,
        ip_addr=ip,
        before=str(before),
        after=str(after)
    )