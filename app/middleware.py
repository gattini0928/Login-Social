from django.shortcuts import redirect

class UsernameRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.username:
            if request.path != '/definir-username/':
                return redirect('definir_username')
        return self.get_response(request)
