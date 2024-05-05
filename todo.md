~~1. list flights (table)~~ full model, proper sizing,
~~4. add flight (form)~~ ~~button~~ css
~~2. update flight (button -> form)~~ popup
~~2a. delete flight (actions part)~~ active reload/invalidation, delete toast
3. populate data tables
3. filterFlight (filter table individually, like example)
5. graphView - graph relations of all flights - nodal

6. solve best path - (input num of destinations to visit)
~~- django models - 5 for the ~~
- django postgres switch (be able to pg_dump) and docker
- connect skiplaggedAPI - https://stackoverflow.com/questions/63422298/how-do-i-scrape-data-using-selenium-in-python-from-a-webpage-that-adds-div-on-sc
- connect skyscannerAPI - https://rapidapi.com/ntd119/api/sky-scanner3
- add airport code db ??? - https://rapidapi.com/leopieters/api/iata-and-icao/
- add button to pull API info into own DB
- display db on frontend
- add form to push form into own DB

MVP: pull API into DB, aggregate DB, display info on frontend via DRF


- remove sort (actions) in table-data
- ensure data validation (min cost < max cost) (ints) (error messages, on submit and while filling out)

- (tracker) arrivals and departures by airport: https://openskynetwork.github.io/opensky-api/rest.html#flights-by-aircraft
- (tracker) 100/month flight tables (to, from, etc) - https://rapidapi.com/flightlookup/api/timetable-lookup/
- (airport codes) airport, airline, airplane info - https://rapidapi.com/leopieters/api/iata-and-icao/
- (pricing ALL) flight pricing from all incl skyscanner: https://rapidapi.com/obryan-software-obryan-software-default/api/compare-flight-prices/
- (pricing ALL) flight pricing, popular directions, 1way - https://rapidapi.com/Travelpayouts/api/flight-data/
- (pricing) skyscanner - https://rapidapi.com/ntd119/api/sky-scanner3
