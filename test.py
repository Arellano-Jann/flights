import numpy as np

OAK = {"OAK" : {
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
}}

MCO = {"MCO" : {
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
    # "MBJ": 129,
    # "PUJ": 179,
}}

ELP = {"ELP" : {
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
}}

HOU = {"HOU" : {
    "ELP": 81,
    "AUS": 92,
    "ATL": 77,
    "DCA": 92,
    "BWI": 89,
    # "PHL": 109,
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
}}

AUS = {"AUS" : {
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
}}

ATL = {"ATL" : {
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
}}

LGA = {"LGA" : {
    "MSY": 84,
    "HOU": 88,
    "DAL": 74,
    "MDW": 64,
    # "ORD": 101,
    "DEN": 95,
    "JAX": 88,
}}

SEA = {"SEA" : {
    "OAK": 53,
    "LAS": 53,
    "PHX": 81,
    "DAL": 91,
    "DEN": 60,
    "MDW": 53,
    # "BNA": 105,
    "BWI": 100,
}}

MDW = {"MDW" : {
    # "ROC": 103,
    "BUF": 97,
    "LGA": 64,
    "BOS": 60,
    "PHL": 89,
    # "BWI": 109,
    "DCA": 78,
    "ATL": 79,
    "MSY": 97,
    "HOU": 82,
    "IAH": 89,
    "DAL": 83,
    # "AUS": 112,
    "SAT": 95,
    "DEN": 89,
    "PDX": 99,
    "SEA": 85,
    "PHX": 99,
    # "RNO": 137,
    # "LAS": 109,
    # "SMF": 111,
    "OAK": 92,
    # "SAN": 138,
    # "MBJ": 174,
}}

BWI = {"BWI" : {
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
}}

DEN = {"DEN" : {
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
    "BWI": 97,
    "IAD": 92,
    "PHL": 98,
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
}}

PDX = {"PDX" : {
    "SMF": 79,
    # "OAK": 109,
    "SJC": 74,
    "SAN": 93,
    "DEN": 88,
    # "SEA": 141,
    "LAS": 99,
    # "PHX": 113,
    # "MDW": 122,
    # "DAL": 123,
}}

CUN = {"CUN" : {
    "MCO": 190,
    "BWI": 212,
    "MDW": 201,
    # "ORD": 274,
    "DEN": 237,
    "PHX": 230,
    "MSY": 204,
    "AUS": 212,
    "SAT": 222,
    "HOU": 198,
}}

MBJ = {"MBJ" : {
    "MCO": 195,
    "BWI": 249,
    # "MDW": 305,
    # "HOU": 305,
}}

PUJ = {"PUJ" : {
    "MCO": 357,
    "BWI": 362,
    "MDW": 368,
    # "HOU": 416,
    # "DEN": 381,
}}

SJO = {"SJO" : {
    "MCO": 297,
    # "BWI": 339,
    "HOU": 250,
    "DEN": 302,
}}


# Extract unique airports from all dictionaries
all_airports = set()
for distances in [OAK, MCO, ELP, HOU, AUS, ATL, LGA, SEA, MDW, BWI, DEN, PDX, CUN, MBJ, PUJ, SJO]:
    all_airports.update(keys for distances_dict in distances.values() for keys in distances_dict.keys())

# Convert the set of airports to a sorted list
airports = sorted(list(all_airports))
print(all_airports)
print(airports)

# Create a matrix filled with NaN values
distance_matrix = np.full((len(airports), len(airports)), np.nan)

# Fill in the matrix with distances
for i, source in enumerate(airports):
    for j, destination in enumerate(airports):
        if source != destination:
            for distances in [OAK, MCO, ELP, HOU, AUS, ATL, LGA, SEA, MDW, BWI, DEN, PDX, CUN, MBJ, PUJ, SJO]:
                if (source in distances and destination in distances[source]):
                    distance_matrix[i, j] = distances.get(source, {}).get(destination, np.nan)
                if (destination in distances and source in distances[destination]):
                    distance_matrix[j, i] = distances.get(destination, {}).get(source, np.nan)
                    break

import pandas
df = pandas.DataFrame(distance_matrix, columns=airports, index=airports)
df = df.fillna('-')
print(df)
df.to_csv('output.csv')