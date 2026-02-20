import logging
from django.utils import timezone
from django.contrib.auth import logout
from django.conf import settings
from datetime import timedelta

logger = logging.getLogger('django.security')

class InactivityTimeoutMiddleware:
    """
    Middleware to log out users after inactivity period.
    Shows warning at 40 minutes, logs out at 45 minutes.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.inactivity_timeout = settings.INACTIVITY_TIMEOUT
        self.warning_time = settings.INACTIVITY_WARNING
    
    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            now = timezone.now().timestamp()
            
            if last_activity is None:
                # First request - set last activity
                request.session['last_activity'] = now
            else:
                # Check inactivity
                time_since_activity = now - last_activity
                
                if time_since_activity > self.inactivity_timeout:
                    # User has been inactive for more than 45 minutes
                    logger.warning(f"User {request.user.username} logged out due to inactivity")
                    logout(request)
                    request.session['session_expired'] = True
                    request.session['inactivity_timeout'] = True
                else:
                    # Update last activity on each request
                    request.session['last_activity'] = now
                    request.session['remaining_time'] = int(self.inactivity_timeout - time_since_activity)
        
        response = self.get_response(request)
        return response
