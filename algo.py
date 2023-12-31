import numpy as np
from first_number_data_modified import airport_data

# import json
# f = open('first_number_data_modified.json')
# airport_data = json.load(f)
# f.close()

# make data into standardized
def read_flight_data(file_path):
    airport_dicts = {}
    current_airport = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("dict"):
                current_airport = line.split()[1]
                airport_dicts[current_airport] = {}
            elif line not in '{}':
                destination, price_range = map(str.strip, line.split(':', 1))
                airport_dicts[current_airport][destination.strip('\"')] = price_range

    return airport_dicts

file_path = 'data_files/data.txt'
flight_data = read_flight_data(file_path)
# print(flight_data)

import json
with open('output/source_flight_data.json', 'w', encoding='utf-8') as f:
    json.dump(flight_data, f, ensure_ascii=False, indent=4)
    
    
    
    
    
####################################################################

# Turn flight_data into numbers or whatever you told chatGPT to do






####################################################################


# Extract unique airports from all dictionaries
all_airports = set()
all_airports.update(airport_data.keys())
for distances in airport_data:
    all_airports.update(airport_data[distances].keys())
    # all_airports.update(keys for distances_dict in distances.values() for keys in distances_dict.keys())

# Convert the set of airports to a sorted list
airports = sorted(list(all_airports))
# print(all_airports)
# print(airports)
# print('adk', airport_data.keys())
# print(airport_data["SJO"])
# print(airport_data["SJO"]["DEN"])

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

# Backfill    
for i in range(len(airports)):
    for j in range(len(airports)):
        # print(np.isnan(distance_matrix[i, j]))
        if (np.isnan(distance_matrix[i, j])): 
            # print('ij',distance_matrix[i, j],'ji',distance_matrix[j, i])
            distance_matrix[i, j] = distance_matrix[j, i]
        if (np.isnan(distance_matrix[j, i])): 
            distance_matrix[j, i] = distance_matrix[i, j]
                
import pandas
df = pandas.DataFrame(distance_matrix, columns=airports, index=airports)

import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize = (12,12)) # size of plot
heatmap = sns.heatmap(df, annot=True, linewidths=1, linecolor='black')
heatmap.get_figure().savefig('output/adj_matrix_heatmap')

df = df.fillna('-')
print(df)
df.to_csv('output/adj_matrix.csv')


####################################################################


def dataframe_to_adjacency_list(df):
    adjacency_list = {}

    # Iterate over rows (nodes)
    for node in df.index:
        neighbors = {}

        # Iterate over columns (potential neighbors)
        for neighbor in df.columns:
            # Check if there's a connection (non-zero weight)
            weight = df.at[node, neighbor]
            if weight != '-':
                neighbors[neighbor] = int(weight)

        adjacency_list[node] = dict(sorted(neighbors.items(),key=lambda x: x[1]))

    return adjacency_list

# Convert DataFrame to adjacency list
adjacency_list = dataframe_to_adjacency_list(df)

# Output the adjacency list
import json
with open('output/adj_list.json', 'w', encoding='utf-8') as f:
    json.dump(adjacency_list, f, ensure_ascii=False, indent=4)
    
    
    
####################################################################
    
    
    
# Find the n least expensive airports to fly from a destination airport to source airport
# Credit to Lyssie
MAX_PRICE_DIFFERENCE = 100 # threshold
# get set of all the children
airport_parents = set(airport_data.keys()) # DEPARTURE
airport_children = set() # ARRIVAL
for parent in airport_parents:
    #print(set(airport_data[parent]))
    airport_children.update(set(airport_data[parent]))
# for each of the child keys
all_airport_connections = {}
cutoff_airport_connections = {}
for child in airport_children:
    # store (parent, int) tuples
    airport_connections = []
    for parent in airport_parents:
        if child in airport_data[parent].keys():
            airport_connections.append( (parent, airport_data[parent][child]) )
    # sort by smallest int
    # print(airport_connections)
    # sort "in place"
    airport_connections = sorted(airport_connections,key=lambda x: x[1])
    all_airport_connections[child] = airport_connections
    # cutoff!!
    # get min
    minimum = min([t[1] for t in airport_connections])
    cutoff = [t for t in all_airport_connections[child] if t[1] <= minimum + MAX_PRICE_DIFFERENCE]
    # print('cutoff', cutoff)
    cutoff_airport_connections[child] = dict(cutoff)
print(cutoff_airport_connections)

import json
with open('output/least_expensive_airports.json', 'w', encoding='utf-8') as f:
    json.dump(dict(sorted(cutoff_airport_connections.items())), f, ensure_ascii=False, indent=4)
    # json.dump(((cutoff_airport_connections)), f, ensure_ascii=False, indent=4)



# # Create new graph

# import networkx as nx
# import matplotlib.pyplot as plt

# # Create a graph object
# G = nx.from_pandas_edgelist(df, airports, airports)

# # # Add nodes to the graph
# # num_nodes = len(matrix)
# # G.add_nodes_from(range(1, num_nodes + 1))

# # # Add edges to the graph based on the matrix
# # for i in range(num_nodes):
# #     for j in range(i + 1, num_nodes):
# #         if matrix[i][j] == 1:
# #             G.add_edge(i + 1, j + 1)

# # Draw the graph
# pos = nx.spring_layout(G)  # You can choose a different layout if needed
# nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8, width=2)

# # Display the graph
# plt.savefig('output.png')