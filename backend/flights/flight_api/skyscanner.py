import requests



from_source = 'YTO'
to_destination = 'DXB'
depart_date = '2020-08-21'
return_date = ''
counts_adults = 1
counts_children = ''

API_URL = 'https://skiplagged.com/api/search.php?from=' + str(from_source) + '&to=' + str(to_destination) + '&depart=' + str(depart_date) + '&'\
       'return=' + str(return_date) + '&format=v3&counts%5Badults%5D=' + str(counts_adults) + '&counts%5Bchildren%5D=' + str(counts_children)
print('URL created: ',API_URL)
flights_details = requests.get(API_URL,verify=False).json()

for flight_number in flights_details['itineraries']['outbound']:
    print('-' * 100)
    print('Flight Number : ',flight_number['flight'])
    print('Flight Price : ', flight_number['one_way_price'])
    number = flight_number['flight']
    print('Flight Details : ',flights_details['flights'][number])
    print('-' * 100) 