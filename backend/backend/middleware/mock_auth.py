from django.contrib.auth import get_user_model
from django.utils.deprecation import MiddlewareMixin

User = get_user_model()

class MockAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        username = request.headers.get('X-User')
        if username:
            try:
                user = User.objects.get(username=username)
                request.user = user
            except User.DoesNotExist:
                pass
