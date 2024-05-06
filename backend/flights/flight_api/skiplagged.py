import requests
from _utils import todays_date, add_days_to_today

class Skiplagged():
    def __init__(self, base_url='https://skiplagged.com/api/search.php', headers=None, *args, **kwargs) -> None:
        self.base_url = base_url
        if not headers:
            self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/46.0.2490.80',
            'Accept': 'application/json'
            }
        else:
            self.headers = headers
        self.querystring = {
            "from": None,
            "to": None,
            "depart": None,
            "return": None,
            "format": "v3",
            "counts%5Badults%5D": None,
            "counts%5Bchildren%5D": None,
            "sort": None
        }
        self.query_results = None
        
    def search(
        self, 
        from_source: str = "LAX", 
        to_destination: str = "NYC", 
        depart_date: str = None, 
        return_date: str = None,
        adult_count: str = '1',
        child_count: str = '0',
        sort: str = 'cost' # cost, duration, path
    ):
        """_summary_

        Args:
            duration (_type_): _description_
            path (_type_): _description_
            from_source (str, optional): _description_. Defaults to "LAX".
            to_destination (str, optional): _description_. Defaults to "NYC".
            depart_date (str, optional): _description_. Defaults to None.
            return_date (str, optional): _description_. Defaults to None.
            adult_count (str, optional): _description_. Defaults to '1'.
            child_count (str, optional): _description_. Defaults to '0'.
            sort (str, optional): _description_. Defaults to 'cost'#cost.

        Returns:
            _type_: _description_
        """
        if depart_date is None:
            depart_date = todays_date()
        if return_date is None:
            return_date = add_days_to_today()
            
        self.querystring = {
            "from": str(from_source),
            "to": str(to_destination),
            "depart": str(depart_date),
            "return": str(return_date),
            "format": "v3",
            "counts%5Badults%5D": str(adult_count),
            "counts%5Bchildren%5D": str(child_count),
            "sort": str(sort)
        }
        response = requests.get(self.base_url, params=self.querystring, headers=self.headers, verify=False)
        print('URL created: ', response.url)
        # print(response.content)
        
        flight_search = response.json()
        
        for flight_key in flight_search['itineraries']['outbound']:
            print('-' * 100)
            print('Flight Number : ', flight_key.get('flight', None))
            print('Flight Price : ', flight_key.get('one_way_price', 99999))
            number = flight_key['flight']
            print('Flight Details : ', flight_search['flights'][number])
            print('-' * 100) 
        
        self.query_results = flight_search
        return flight_search
    
    def get_flight_segment(self, flight_key: str):
        # return self.query_results['flights'][flight_key]['segments']
        flights = self.query_results.get('flights', {})
        flight_data = flights.get(flight_key, {})
        segments = flight_data.get('segments', [])
        return segments
    
    def get_source_airport(self, flight_key: str):
        # return self.query_results['flights'][flight_key]['segments'][0]['departure']['airport']
        flights = self.query_results.get('flights', {})
        flight_data = flights.get(flight_key, {})
        segments = flight_data.get('segments', [])
        first_segment = segments[0] if segments else {}
        departure = first_segment.get('departure', {})
        airport = departure.get('airport', None)
        return airport
    
    def get_dest_airport(self, flight_key: str):
        # return self.query_results['flights'][flight_key]['segments'][-1]['arrival']['airport']
        flights = self.query_results.get('flights', {})
        flight_data = flights.get(flight_key, {})
        segments = flight_data.get('segments', [])
        last_segment = segments[-1] if segments else {}
        arrival = last_segment.get('arrival', {})
        airport = arrival.get('airport', None)
        return airport
    
    def get_lowest_price(self, num: int = 1):
        """Gets the num lowest flights by price

        Args:
            num (int): number of flights to return
        """
        lowest_prices = {}
        outbound_flights = self.query_results['itineraries']['outbound']
        sorted_outbound_flights = sorted(outbound_flights, key=lambda x: x['one_way_price'])
        for flight in sorted_outbound_flights[:num]:
            flight_key = flight['flight']
            flight_details = {
                'segments': self.get_flight_segment(flight_key),
                'one_way_price': flight.get('one_way_price', 99999),
                'from_source': self.get_source_airport(flight_key),
                'to_dest': self.get_dest_airport(flight_key),
            }
            lowest_prices[flight_key] = flight_details
        
        return 
    
    def get_iata_codes(self):
        iata_codes = {
            "from_iata": self.querystring.get('from', None),
            "to_iata": self.querystring.get('to', None),
        }
        return iata_codes
        
        
skiplagged = Skiplagged()
        
# Call search method
skiplagged.search(from_source="LAX", to_destination="NYC")

# Check if querystring is set correctly
# assert skiplagged.querystring["from"] == "LAX"
# assert skiplagged.querystring["to"] == "NYC"
print (skiplagged.querystring["from"] == "LAX")
print (skiplagged.querystring["to"] == "NYC")
print (skiplagged.querystring["from"])
print (skiplagged.querystring["to"])

# Check if query results are stored correctly
# print (skiplagged.query_results)