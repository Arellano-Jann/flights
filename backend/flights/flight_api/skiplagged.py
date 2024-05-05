import requests
from ._utils import todays_date, add_days_to_today

class Skiplagged():
    def __init__(self, base_url='https://skiplagged.com/api/search.php?', headers=None, *args, **kwargs) -> None:
        self.base_url = base_url
        self.headers = headers
        
    def search(
        self, 
        from_source: str = "LAX", 
        to_destination: str = "NYC", 
        depart_date: str = None, 
        return_date: str = None,
        adult_count: str = '1',
        child_count: str = '0',
    ):
        if depart_date is None:
            depart_date = todays_date()
        if return_date is None:
            return_date = add_days_to_today()
        
        API_URL = self.base_url + 'from=' + str(from_source) + '&to=' + str(to_destination) + '&depart=' + str(depart_date) + '&'\
            'return=' + str(return_date) + '&format=v3&counts%5Badults%5D=' + str(adult_count) + '&counts%5Bchildren%5D=' + str(child_count)
        print('URL created: ', API_URL)
        
        flight_search = requests.get(API_URL)
        flight_search = flight_search.json()
        
        for flight_number in flight_search['itineraries']['outbound']:
            print('-' * 100)
            print('Flight Number : ', flight_number['flight'])
            print('Flight Price : ', flight_number['one_way_price'])
            number = flight_number['flight']
            print('Flight Details : ', flight_search['flights'][number])
            print('-' * 100) 
        flight_number = flight_number['flight']
        flight_price = flight_number
        return flight_search, 