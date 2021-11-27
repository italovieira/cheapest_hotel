from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


GET_CHEAPEST_URL = reverse('hotel:cheapest')

class GetCheapestTests(APITestCase):
    """API test for get cheapest booking hotel endpoint"""

    def test_get_cheapest_with_no_input(self):
        """Make a request without input and expects a error response"""
        response = self.client.get(GET_CHEAPEST_URL)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_cheapest_with_incorrect_input(self):
        """Make a request with incorrect input and expects a error response"""
        request_input = 'qualq:uer&c(oisaaqu)iparad{are}rrado'
        response = self.client.get(GET_CHEAPEST_URL, {'input': request_input})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_successful_get_cheapest(self):
        """Make a request with correct input and expects a successful response"""
        request_input = 'Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'
        response = self.client.get(GET_CHEAPEST_URL, {'input': request_input})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_cheapest_lakewood_result(self):
        """Make a request and expects Lakewood as result"""
        request_input = 'Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'
        response = self.client.get(GET_CHEAPEST_URL, {'input': request_input})
        self.assertEqual(response.data, {'cheapest': 'Lakewood'})

    def test_get_cheapest_bridgewood_result(self):
        """Make a request and expects Bridgewood as result"""
        request_input = 'Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)'
        response = self.client.get(GET_CHEAPEST_URL, {'input': request_input})
        self.assertEqual(response.data, {'cheapest': 'Bridgewood'})

    def test_get_cheapest_ridgewood_result(self):
        """Make a request and expects Ridgewood as result"""
        request_input = 'Reward: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)'
        response = self.client.get(GET_CHEAPEST_URL, {'input': request_input})
        self.assertEqual(response.data, {'cheapest': 'Ridgewood'})
