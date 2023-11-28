import numpy as np
from first_number_data_modified import airport_data


# Extract unique airports from all dictionaries
all_airports = set()
for distances in airport_data:
    all_airports.update(airport_data[distances].keys())
    # all_airports.update(keys for distances_dict in distances.values() for keys in distances_dict.keys())

# Convert the set of airports to a sorted list
airports = sorted(list(all_airports))
print(all_airports)
print(airports)
print('adk', airport_data.keys())
print(airport_data["SJO"])
print(airport_data["SJO"]["DEN"])

# Create a matrix filled with NaN values
distance_matrix = np.full((len(airports), len(airports)), np.nan)

# Fill in the matrix with distances
for i, source in enumerate(airports):
    for j, destination in enumerate(airports):
        if source != destination:
            # # METHOD 1 FOR
            # # OAK = {"OAK" : {
            # #     # "SJO": 347,
            # #     "LGA": 95,
            # #     "HNL": 119,
            # #     "SEA": 53,
            # #     "BWI": 102,
            # #     "MDW": 64,
            # #     # "ATL": 120,
            # #     "AUS": 73,
            # #     # "IAH": 154,
            # #     # "HOU": 150,
            # # }}
            # for distances in [OAK, MCO, ELP, HOU, AUS, ATL, LGA, SEA, MDW, BWI, DEN, PDX, CUN, MBJ, PUJ, SJO]:
            #     if (source in distances and destination in distances[source]): # if source is a departure and destination is in the list of flights the source can do
            #         distance_matrix[i, j] = distances.get(source, {}).get(destination, np.nan)
            #     if (destination in distances and source in distances[destination]):
            #         distance_matrix[j, i] = distances.get(destination, {}).get(source, np.nan)
            #         break
            
            # METHOD 2
            if (source in airport_data.keys() and destination in airport_data[source]):
                distance_matrix[i, j] = airport_data.get(source, {}).get(destination, np.nan)
            if (destination in airport_data.keys() and source in airport_data[destination]):
                distance_matrix[j, i] = airport_data.get(destination, {}).get(source, np.nan)

import pandas
df = pandas.DataFrame(distance_matrix, columns=airports, index=airports)
df = df.fillna('-')
print(df)
df.to_csv('output.csv')