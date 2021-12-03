from rest_framework import views
from rest_framework.response import Response


class CheapestHotelView(views.APIView):
    def get(self, request):
        return Response({})
