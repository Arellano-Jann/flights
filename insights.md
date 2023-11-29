# BASE INFO 
DEPARTURES
['OAK', 'SJO', 'MCO', ['ELP', 'HOU', 'AUS',], 'ATL', 'LGA', 'MDW', 'BWI', 'DEN', 'SEA', 'PDX', 'CUN', 'MBJ', 'PUJ']

ALL AIRPORTS
['ATL', 'AUS', 'BOS', 'BUF', 'BWI', 'CUN', 'DAL', 'DCA', 'DEN', 'ELP', 'HNL', 'HOU', 'IAD', 'IAH', 'JAX', 'LAS', 'LGA', 'MBJ', 'MCO', 'MDW', 'MSY', 'OAK', 'ORD', 'PDX', 'PHL', 'PHX', 'RNO', 'SAN', 'SEA', 'SFO', 'SJC', 'SJO', 'SMF']

REQUIRED
['SJO', 'MCO', ['ELP', 'HOU', 'AUS',], 'ATL', 'LGA', 'MDW', 'SEA', ['OAK', 'LAS']]
['DEN', 'MSY', 'PDX']


# BROKEN UP

ATL to LGA Route[
    BOS to SEA Short Route
    396 -> [OAK, LAS]
    60  -> 64  -> 78  -> 46 ->  95  -> 53  -> OAK -> RNO
    ATL -> LGA -> MDW -> BOS -> BWI -> SEA -> OAK -> RNO

    DCA to SEA Long Route
    471 -> [OAK, LAS]
    60  -> 64  -> 78  -> 67  -> 59  -> 90  -> 53  -> [OAK, LAS]
    ATL -> LGA -> MDW -> DCA -> MCO -> MSY -> SEA -> [OAK, LAS]
]

LGA to ATL Route[
    347 -> OAK -> RNO
    60  -> 79  -> 60  -> 46  -> 102 -> OAK -> RNO
    LGA -> ATL -> MDW -> BOS -> BWI -> OAK -> RNO

]

MDW -> BWI Short Route
MDW -> BOS -> BWI -> OAK 
60  -> 46  -> 102 -> OAK -> RNO
208 -> OAK -> RNO

END
---------------------------------------
START

SJO to MCO Route[
    AUS to MDW Route
    391 -> ATL to LGA Routes
    206 -> 59  -> 66  ->  60 -> 79  -> ATL to LGA Routes
    SJO -> MCO -> AUS -> BOS -> MDW -> ATL to LGA Routes

    AUS to MDW Route
    455 -> LGA to ATL Routes
    206 -> 59  -> 66  ->  60 ->  64 -> LGA to ATL Routes
    SJO -> MCO -> AUS -> BOS -> MDW -> LGA to ATL Routes

    AUS to BWI Route
    436 -> ATL to LGA Routes
    206 -> 59  -> 66  ->  46 -> 59  -> ATL to LGA Routes
    SJO -> MCO -> AUS -> BOS -> BWI -> ATL to LGA Routes

    AUS to BWI Route
    461 -> ATL to LGA Routes
    206 -> 59  -> 66  ->  46 -> 84  -> LGA to ATL Routes
    SJO -> MCO -> AUS -> BOS -> BWI -> LGA to ATL Routes

    MSY to AUS Short Route
    406 -> ATL to LGA Routes
    206 -> 59  -> 60  ->  81 -> ATL to LGA Routes
    SJO -> MCO -> MSY -> AUS -> ATL to LGA Routes

    MSY to DEN Long Route
    537 -> LGA to ATL Routes
    206 -> 59  -> 60  -> 60  -> 81  -> 71  -> LGA to ATL Routes
    SJO -> MCO -> MSY -> AUS -> ELP -> DEN -> LGA to ATL Routes
]

SJO to ATL Route
336 -> LGA to ATL Routes
199 -> 77  -> 60  -> LGA to ATL Routes
SJO -> HOU -> ATL -> LGA to ATL Routes

-------------

# ROUTE OPTIONS

ROUTE 1.0
391 + OAK -> RNO
206 -> 59  -> 66  ->  60 -> ATL to LGA or LGA to ATL Routes
SJO -> MCO -> AUS -> BOS -> MDW -> ATL to LGA or LGA to ATL Routes
['ATL', 'AUS', '', 'BUF', 'BWI', 'CUN', 'DAL', 'DCA', 'DEN', 'ELP', 'HNL', 'HOU', 'IAD', 'IAH', 'JAX', 'LAS', 'LGA', 'MBJ', '', 'MSY', 'OAK', 'ORD', 'PDX', 'PHL', 'PHX', 'RNO', 'SAN', 'SEA', 'SFO', 'SJC', 'SMF']
['', '', ['ELP', 'HOU', '',], 'ATL', 'LGA', '', 'SEA', ['OAK', 'LAS']]
['DEN', 'MSY', 'PDX']

ROUTE 1.1
436 + OAK -> RNO
206 -> 59  -> 66  ->  46 -> 59  -> ATL to LGA Routes
SJO -> MCO -> AUS -> BOS -> BWI -> ATL -> ATL to LGA Routes
[   'BUF',  'CUN', 'DAL', 'DCA', 'DEN', 'ELP', 'HNL', 'HOU', 'IAD', 'IAH', 'JAX', 'LAS', 'LGA', 'MBJ', 'MDW', 'MSY', 'OAK', 'ORD', 'PDX', 'PHL', 'PHX', 'RNO', 'SAN', 'SEA', 'SFO', 'SJC', 'SMF']
[  ['ELP', 'HOU', ],  'LGA', 'MDW', 'SEA', ['OAK', 'LAS']]
['DEN', 'MSY', 'PDX']

ROUTE 1.2
802 + OAK -> RNO
206 -> 59  -> 60  ->  81 -> 60  -> 64  -> 78  -> 46  -> 95  -> 53  -> OAK -> RNO
SJO -> MCO -> MSY -> AUS -> ATL -> LGA -> MDW -> BOS -> BWI -> SEA -> OAK -> RNO
['BUF', 'CUN', 'DAL', 'DCA', 'DEN', 'ELP', 'HNL', 'HOU', 'IAD', 'IAH', 'JAX', 'LAS', 'MBJ', 'ORD', 'PDX', 'PHL', 'PHX', 'SAN', 'SFO', 'SJC', 'SMF']
[['ELP', 'HOU', ['LAS']]]
['DEN', 'PDX']

ROUTE 1.3
930 -> OAK -> RNO
SJO -> MCO -> MSY -> AUS -> ELP -> DEN -> LGA -> ATL -> MDW -> BOS -> BWI -> SEA -> OAK -> RNO
206  -> 59 -> 60  -> 60  -> 81  -> 71  -> 60  -> 79  -> 60  -> 46  -> 95  -> 53  -> OAK -> RNO
['BUF','CUN', 'DAL', 'DCA','HNL', 'HOU', 'IAD', 'IAH', 'JAX', 'LAS', '', 'MBJ', 'ORD', 'PDX', 'PHL', 'PHX', 'RNO', 'SAN', 'SEA', 'SFO', 'SJC', 'SMF']
[[ 'HOU', ],[ 'LAS']]
['PDX']

ROUTE 1.4
884 -> OAK -> RNO
206  -> 59 -> 60  -> 60  -> 81  -> 71  -> 60  -> 79  -> 60  -> 46  -> 102 -> OAK -> RNO
SJO -> MCO -> MSY -> AUS -> ELP -> DEN -> LGA -> ATL -> MDW -> BOS -> BWI -> OAK -> RNO
['BUF','CUN', 'DAL', 'DCA','HNL', 'HOU', 'IAD', 'IAH', 'JAX', 'LAS', '', 'MBJ', 'ORD', 'PDX', 'PHL', 'PHX', 'RNO', 'SAN', 'SEA', 'SFO', 'SJC', 'SMF']
[[ 'HOU', ],[ 'LAS']]
['PDX']


ROUTE 2.1
725 + OAK -> RNO
199  -> 77  -> 60  -> 64  -> 78  -> 46 -> 95  -> 53  -> OAK -> RNO
SJO -> HOU -> ATL -> LGA -> MDW -> BOS -> BWI -> SEA -> OAK -> RNO
['AUS', 'BUF', 'CUN', 'DAL', 'DCA', 'DEN', 'ELP', 'HNL', 'IAD', 'IAH', 'JAX', 'LAS', 'MBJ', 'MCO', 'MSY', 'ORD', 'PDX', 'PHL', 'PHX', 'SAN', 'SFO', 'SJC', 'SMF']
['MCO', ['ELP', 'AUS',], ['LAS']]
['DEN', 'MSY', 'PDX']

ROUTE 2.2
747 + OAK -> RNO
199  -> 77  -> 60  -> 64  -> 78  -> 67  -> 59  -> 90  -> 53  -> [OAK, LAS]
SJO  -> HOU -> ATL -> LGA -> MDW -> DCA -> MCO -> MSY -> SEA -> [OAK, LAS]
['AUS', 'BOS', 'BUF', 'BWI', 'CUN', 'DAL', 'DEN', 'ELP', 'HNL', 'IAD', 'IAH', 'JAX', 'MBJ', 'ORD', 'PDX', 'PHL', 'PHX', 'RNO', 'SAN', 'SFO', 'SJC', 'SMF']
[['ELP', 'AUS']]
['DEN', 'PDX']