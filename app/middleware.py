from django.shortcuts import redirect
from django.urls import reverse

class UsernameRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            username = request.user.username
            if not username:
                definir_username_url = reverse('definir_username')
                if request.path != definir_username_url:
                    return redirect(definir_username_url)
        return self.get_response(request)

