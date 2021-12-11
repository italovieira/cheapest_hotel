import re

from django.utils.http import MONTHS

from datetime import datetime


_client_regex = r'(regular|reward)'
_date_regex = rf'(\d{{2}}(?:{"|".join(MONTHS)})\d{{4}})(?:\(\w*\))?(?:,|$)'

def validate_input(input_data):
    normalized_input = input_data.replace(r' ', '').lower()
    input_pattern = re.compile(f'^{_client_regex}:({_date_regex})+$')
    matching = input_pattern.match(normalized_input)
    return '' if matching is None else matching.string

def parse_input(input_data):
    validated_input = validate_input(input_data)
    client_pattern = re.compile(f'{_client_regex}:(.*)')
    client, dates_input = client_pattern.match(validated_input).groups()

    dates_pattern = re.compile(_date_regex)
    dates = dates_pattern.findall(dates_input)

    def parse_date(date):
        return datetime.strptime(date, '%d%b%Y')

    return client, (parse_date(date) for date in dates)
