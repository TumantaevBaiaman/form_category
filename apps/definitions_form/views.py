from rest_framework.views import APIView
from . import logic


class CreateForm(APIView):

    def post(self, request):
        return logic.create_form(request)


class GetForm(APIView):

    def post(self, request):
        return logic.get_form(request)
