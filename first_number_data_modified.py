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
# 802 + OAK -> RNO
# 206 -> 59  -> 60  ->  81 -> 60  -> 64  -> 78  -> 46  -> 95  -> 53  -> OAK -> RNO
# SJO -> MCO -> MSY -> AUS -> ATL -> LGA -> MDW -> BOS -> BWI -> SEA -> OAK -> RNO
# ['BUF', 'CUN', 'DAL', 'DCA', 'DEN', 'ELP', 'HNL', 'HOU', 'IAD', 'IAH', 'JAX', 'LAS', 'LGA', 'MBJ', 'MSY', 'ORD', 'PDX', 'PHL', 'PHX', 'SAN', 'SFO', 'SJC', 'SMF']
# [['ELP', 'HOU', ['LAS']]
# ['DEN', 'PDX']

# ROUTE 1.3
# SJO -> MCO -> MSY -> AUS -> ELP -> DEN ->
# 206  -> 59  -> 60  -> 00  -> 00  -> 00 -> 00  -> 00  -> 00  -> OAK -> RNO
# ['ATL', '', 'BOS', 'BUF', 'BWI', 'CUN', 'DAL', 'DCA', '', '', 'HNL', 'HOU', 'IAD', 'IAH', 'JAX', 'LAS', 'LGA', 'MBJ', 'MDW', 'MSY', 'OAK', 'ORD', 'PDX', 'PHL', 'PHX', 'RNO', 'SAN', 'SEA', 'SFO', 'SJC', 'SMF']
# ['', '', ['', 'HOU', '',], 'ATL', 'LGA', 'MDW', 'SEA', ['OAK', 'LAS']]
# ['', '', 'PDX']

# ROUTE 2.1
# 725 + OAK -> RNO
# 199  -> 77  -> 60  -> 64  -> 78  -> 46 -> 95  -> 53  -> OAK -> RNO
# SJO -> HOU -> ATL -> LGA -> MDW -> BOS -> BWI -> SEA -> OAK -> RNO
# ['AUS', 'BUF', 'CUN', 'DAL', 'DCA', 'DEN', 'ELP', 'HNL', 'IAD', 'IAH', 'JAX', 'LAS', 'MBJ', 'MCO', 'MSY', 'ORD', 'PDX', 'PHL', 'PHX', 'SAN', 'SFO', 'SJC', 'SMF']
# ['MCO', ['ELP', 'AUS',], ['LAS']]
# ['DEN', 'MSY', 'PDX']

# ROUTE 2.2
# 747 + OAK -> RNO
# 199  -> 77  -> 60  -> 64  -> 78  -> 67  -> 59  -> 90  -> 53  -> [OAK, LAS]
# SJO  -> HOU -> ATL -> LGA -> MDW -> DCA -> MCO -> MSY -> SEA -> [OAK, LAS]
# ['AUS', 'BOS', 'BUF', 'BWI', 'CUN', 'DAL', 'DEN', 'ELP', 'HNL', 'IAD', 'IAH', 'JAX', 'MBJ', 'ORD', 'PDX', 'PHL', 'PHX', 'RNO', 'SAN', 'SFO', 'SJC', 'SMF']
# [['ELP', 'AUS']]
# ['DEN', 'PDX']

airport_data = { 
    "OAK": {
        # "SJO": 347,
        "LGA": 95,
        "HNL": 119,
        "SEA": 53,
        "BWI": 102,
        "MDW": 64,
        # "ATL": 120,
        "AUS": 73,
        # "IAH": 154,
        # "HOU": 150,
    },
    "MCO": {
        # "SJO": 273,
        "AUS": 53,
        "IAH": 89,
        "HOU": 88,
        # "ELP": 123,
        "ATL": 88,
        "DCA": 67,
        # "BWI": 114,
        "PHL": 89,
        # "DEN": 129,
        "ORD": 89,
        "MDW": 89,
        "MSY": 59,
        # "ISP": 114,
        "SMF": 98,
        # "NAS": 132,
        # "CUN": 136,
        "MBJ": 129,
        # "PUJ": 179,
    },
    "ELP": {
        # "MDW": 123,
        # "ORD": 118,
        "DEN": 81,
        # "MCO": 133,
        # "JAX": 156,
        "HOU": 81,
        "IAH": 91,
        "AUS": 60,
        "PHX": 67,
        # "LAS": 104,
        # "SAN": 113,
    },
    "HOU": {
        "ELP": 81,
        "AUS": 92,
        "ATL": 77,
        "DCA": 92,
        "BWI": 89,
        "PHL": 109,
        "LGA": 88,
        "MDW": 82,
        "DEN": 89,
        # "SMF": 132,
        # "OAK": 150,
        # "SJC": 132,
        # "SAN": 151,
        "PHX": 89,
        # "BZE": 145,
        # "SJO": 168,
        "CUN": 95,
        # "MBJ": 185,
    },
    "AUS": {
        "BOS": 66,
        # "BWI": 109,
        "DCA": 92,
        # "IAD": 102,
        # "MDW": 112,
        # "ORD": 112,
        "ATL": 81,
        "MSY": 60,
        "DEN": 89,
        "ELP": 60,
        "HOU": 92,
        "PHX": 83,
        "LAS": 74,
        "SAN": 67,
        "OAK": 73,
        "SJC": 67,
        "SMF": 89,
        # "CUN": 128,
    },
    "ATL": {
        "JAX": 92,
        "MSY": 81,
        "HOU": 99,
        "AUS": 81,
        "DAL": 89,
        "DCA": 78,
        "BWI": 79,
        "PHL": 87,
        "LGA": 60,
        "MDW": 79,
        "DEN": 67,
        # "OAK": 119,
        # "SAN": 108,
        # "LAS": 140,
        # "CUN": 157,
    },
    "LGA": {
        "MSY": 84,
        "HOU": 88,
        "DAL": 74,
        "MDW": 64,
        # "ORD": 101,
        # "DEN": 95,
        "JAX": 88,
    },
    "SEA": {
        "OAK": 53,
        "LAS": 53,
        # "PHX": 81,
        # "DAL": 91,
        "DEN": 60,
        "MDW": 53,
        # "BNA": 105,
        # "BWI": 100,
    },
    "MDW": {
        # "ROC": 103,
        # "BUF": 97,
        "LGA": 64,
        "BOS": 60,
        "PHL": 89,
        # "BWI": 109,
        "DCA": 78,
        "ATL": 79,
        # "MSY": 97,
        "HOU": 82,
        "IAH": 89,
        "DAL": 83,
        # "AUS": 112,
        # "SAT": 95,
        "DEN": 89,
        # "PDX": 99,
        "SEA": 85,
        # "PHX": 99,
        # "RNO": 137,
        # "LAS": 109,
        # "SMF": 111,
        "OAK": 92,
        # "SAN": 138,
        # "MBJ": 174,
    },
    "BWI": {
        # "ISP": 102,
        "LGA": 84,
        # "ROC": 102,
        # "BUF": 109,
        "BOS": 46,
        "MDW": 78,
        "ORD": 78,
        "ATL": 59,
        # "MCO": 114,
        "AUS": 87,
        "DAL": 92,
        # "DEN": 116,
        "SEA": 95,
        "PHX": 89,
        # "LAS": 129,
        # "OAK": 129,
        # "SAN": 123,
        # "SJO": 224,
        # "MBJ": 166,
    },
    "DEN": {
        "SEA": 60,
        "PDX": 53,
        "SMF": 85,
        # "OAK": 138,
        "SJC": 85,
        "SFO": 91,
        "SAN": 89,
        "RNO": 85,
        "LAS": 79,
        "PHX": 79,
        "ELP": 78,
        "AUS": 85,
        "HOU": 89,
        "IAH": 89,
        # "MSY": 109,
        # "MCO": 129,
        # "JAX": 108,
        "ATL": 67,
        # "BWI": 97,
        "IAD": 92,
        # "PHL": 98,
        # "ISP": 185,
        "LGA": 71,
        "BUF": 83,
        "BOS": 84,
        "MDW": 66,
        "ORD": 66,
        # "GRR": 102,
        # "CUN": 109,
        # "BZE": 220,
        # "SJO": 147,
    },
    "PDX": {
        "SMF": 79,
        "OAK": 40,
        "SJC": 53,
        "SAN": 77,
        "DEN": 53,
        # "SEA": 141,
        "LAS": 70,
        "PHX": 60,
        "MDW": 89,
        # "DAL": 101,
    },
    "CUN": {
        "MCO": 160,
        # "BWI": 173,
        "MDW": 137,
        "ORD": 165,
        "DEN": 129,
        # "PHX": 191,
        # "MSY": 176,
        "AUS": 142,
        # "SAT": 183,
        "HOU": 108,
    },
    "MBJ": {
        "MCO": 171,
        # "BWI": 210,
        # "MDW": 218,
        # "HOU": 235,
    },
    # "PUJ": {
    #     "MCO": 220,
    #     "BWI": 217,
    #     "MDW": 211,
    #     "HOU": 227,
    #     # "DEN": 257,
    # },
    "SJO": {
        "MCO": 206,
        "BWI": 211,
        "HOU": 199,
        "DEN": 214,
    },
}