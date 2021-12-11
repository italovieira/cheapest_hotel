from rest_framework import views, status
from rest_framework.response import Response

from hotel.helpers import validate_input


class CheapestHotelView(views.APIView):
    def get(self, request):
        try:
            input_data = request.query_params['input']
        except KeyError:
            return Response({}, status.HTTP_404_NOT_FOUND)
        else:
            if validate_input(input_data):
                pass
            else:
                return Response({}, status.HTTP_400_BAD_REQUEST)
