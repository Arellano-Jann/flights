# DEPARTURES
# ['OAK', 'SJO', 'MCO', ['ELP', 'HOU', 'AUS',], 'ATL', 'LGA', 'MDW', 'BWI', 'DEN', 'SEA', 'PDX', 'CUN', 'MBJ', 'PUJ']

# ALL AIRPORTS
# ['ATL', 'AUS', 'BOS', 'BUF', 'BWI', 'CUN', 'DAL', 'DCA', 'DEN', 'ELP', 'HNL', 'HOU', 'IAD', 'IAH', 'JAX', 'LAS', 'LGA', 'MBJ', 'MCO', 'MDW', 'MSY', 'OAK', 'ORD', 'PDX', 'PHL', 'PHX', 'RNO', 'SAN', 'SEA', 'SFO', 'SJC', 'SJO', 'SMF']

# REQUIRED
# ['SJO', 'MCO', ['ELP', 'HOU', 'AUS',], 'ATL', 'LGA', 'MDW', 'SEA', ['OAK', 'LAS']]
# ['DEN', 'MSY', 'PDX']

# ATL to LGA Route
# ATL -> LGA -> MDW -> BOS -> BWI -> SEA -> OAK -> RNO
# 60  -> 64  -> 78  -> 46 ->  95  -> 53  -> OAK -> RNO
# 396 -> [OAK, LAS]

# ATL -> LGA -> MDW -> DCA -> MCO -> MSY -> SEA -> [OAK, LAS]
# 60  -> 64  -> 78  -> 67  -> 59  -> 90  -> 53  -> [OAK, LAS]
# 471 -> [OAK, LAS]



# ROUTE 1.1
# SJO -> MCO -> AUS
# ['ATL', 'AUS', 'BOS', 'BUF', 'BWI', 'CUN', 'DAL', 'DCA', 'DEN', 'ELP', 'HNL', 'HOU', 'IAD', 'IAH', 'JAX', 'LAS', 'LGA', 'MBJ', 'MDW', 'MSY', 'OAK', 'ORD', 'PDX', 'PHL', 'PHX', 'RNO', 'SAN', 'SEA', 'SFO', 'SJC', 'SMF']
# ['', '', ['ELP', 'HOU', 'AUS',], 'ATL', 'LGA', 'MDW', 'SEA', ['OAK', 'LAS']]
# ['DEN', 'MSY', 'PDX']

# ROUTE 1.2
### 802 + OAK -> RNO
# 206 -> 59  -> 60  ->  81 -> 60  -> 64  -> 78  -> 46  -> 95  -> 53  -> OAK -> RNO
# SJO -> MCO -> MSY -> AUS -> ATL -> LGA -> MDW -> BOS -> BWI -> SEA -> OAK -> RNO
# ['BUF', 'CUN', 'DAL', 'DCA', 'DEN', 'ELP', 'HNL', 'HOU', 'IAD', 'IAH', 'JAX', 'LAS', 'LGA', 'MBJ', 'MSY', 'ORD', 'PDX', 'PHL', 'PHX', 'SAN', 'SFO', 'SJC', 'SMF']
# [['ELP', 'HOU', ['LAS']]]
# ['DEN', 'PDX']

# ROUTE 1.3
# SJO -> MCO -> MSY -> AUS -> ELP -> DEN ->
# 206  -> 59  -> 60  -> 00  -> 00  -> 00 -> 00  -> 00  -> 00  -> OAK -> RNO
# ['ATL', '', 'BOS', 'BUF', 'BWI', 'CUN', 'DAL', 'DCA', '', '', 'HNL', 'HOU', 'IAD', 'IAH', 'JAX', 'LAS', 'LGA', 'MBJ', 'MDW', 'MSY', 'OAK', 'ORD', 'PDX', 'PHL', 'PHX', 'RNO', 'SAN', 'SEA', 'SFO', 'SJC', 'SMF']
# ['', '', ['', 'HOU', '',], 'ATL', 'LGA', 'MDW', 'SEA', ['OAK', 'LAS']]
# ['', '', 'PDX']

# ROUTE 2.1
### 725 + OAK -> RNO
# 199  -> 77  -> 60  -> 64  -> 78  -> 46 -> 95  -> 53  -> OAK -> RNO
# SJO -> HOU -> ATL -> LGA -> MDW -> BOS -> BWI -> SEA -> OAK -> RNO
# ['AUS', 'BUF', 'CUN', 'DAL', 'DCA', 'DEN', 'ELP', 'HNL', 'IAD', 'IAH', 'JAX', 'LAS', 'MBJ', 'MCO', 'MSY', 'ORD', 'PDX', 'PHL', 'PHX', 'SAN', 'SFO', 'SJC', 'SMF']
# ['MCO', ['ELP', 'AUS',], ['LAS']]
# ['DEN', 'MSY', 'PDX']

# ROUTE 2.2
### 747 + OAK -> RNO
# 199  -> 77  -> 60  -> 64  -> 78  -> 67  -> 59  -> 90  -> 53  -> [OAK, LAS]
# SJO  -> HOU -> ATL -> LGA -> MDW -> DCA -> MCO -> MSY -> SEA -> [OAK, LAS]
# ['AUS', 'BOS', 'BUF', 'BWI', 'CUN', 'DAL', 'DEN', 'ELP', 'HNL', 'IAD', 'IAH', 'JAX', 'MBJ', 'ORD', 'PDX', 'PHL', 'PHX', 'RNO', 'SAN', 'SFO', 'SJC', 'SMF']
# [['ELP', 'AUS']]
# ['DEN', 'PDX']