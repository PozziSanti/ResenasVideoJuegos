class InvitadoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            request.session['rol'] = 'invitado'
        else:
            request.session['rol'] = 'usuario'
        return self.get_response(request)