from rest_framework import views, status
from rest_framework.response import Response

from hotel.helpers import parse_input
from hotel.models import Hotel


class CheapestHotelView(views.APIView):
    def get(self, request):
        try:
            input_data = request.query_params['input']
        except KeyError:
            return Response({'error': "expected an 'input' param"}, status.HTTP_404_NOT_FOUND)
        else:
            try:
                client, dates = parse_input(input_data)
                return Response({'cheapest': Hotel.objects.cheapest(client, dates)})
            except:
                return Response({'error': "given 'input' is invalid"}, status.HTTP_400_BAD_REQUEST)
