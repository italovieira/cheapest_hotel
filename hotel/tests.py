from datetime import datetime
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from hotel.helpers import validate_input, parse_input


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


class ValidatorTests(APITestCase):
    """Test for the input validator"""

    def test_validate_invalid_input1(self):
        """Test validator with invalid input"""
        invalid_input = 'islosldlsdéulds9llinpusllln@vá#i@o!'
        self.assertFalse(validate_input(invalid_input))

    def test_validate_invalid_input2(self):
        """Test validator with invalid client type"""
        invalid_input = 'normal: 20Mar2009(fri), 21Mar2009(sat), 10Mar2009(sun)'
        self.assertFalse(validate_input(invalid_input))

    def test_validate_invalid_input3(self):
        """Test validator with invalid date"""
        invalid_input = 'normal: 2Ma2009(fri), 21Mar2009(sat), 10Mar2009(sun)'
        self.assertFalse(validate_input(invalid_input))

    def test_validate_invalid_input4(self):
        """Test validator with invalid separator"""
        invalid_input = 'normal; 2Ma2009(fri), 21Mar2009(sat), 10Mar2009(sun)'
        self.assertFalse(validate_input(invalid_input))

    def test_validate_invalid_input5(self):
        """Test validator with invalid separator for dates"""
        invalid_input = 'reward: 2Ma2009(fri)| 21Mar2009(sat)@ 10Mar2009(sun)'
        self.assertFalse(validate_input(invalid_input))

    def test_validate_valid_input(self):
        """Test validator with valid input"""
        valid_input = 'Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)'
        self.assertEqual(validate_input(valid_input), 'regular:20mar2009(fri),21mar2009(sat),22mar2009(sun)')


class ParserTests(APITestCase):
    """Test for the input parsers"""

    def test_parser_input(self):
        """Test for parse string input"""
        normalized_input = 'regular:20mar2009(fri),21mar2009(sat),22mar2009(sun)'
        client, dates = parse_input(normalized_input)

        self.assertEqual(client, 'regular')
        self.assertEqual(tuple(dates), (
            datetime(2009, 3, 20),
            datetime(2009, 3, 21),
            datetime(2009, 3, 22),
        ))
