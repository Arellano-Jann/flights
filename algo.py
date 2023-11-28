import numpy as np
from first_number_data_modified import airport_data


# Extract unique airports from all dictionaries
all_airports = set()
all_airports.update(airport_data.keys())
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
                neighbors[neighbor] = weight

        adjacency_list[node] = neighbors

    return adjacency_list

# Convert DataFrame to adjacency list
adjacency_list = dataframe_to_adjacency_list(df)

# Output the adjacency list
import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(adjacency_list, f, ensure_ascii=False, indent=4)





def find_minimum_values(data, threshold):
    with open("minimum_output.txt", "w") as file:
        for source, destinations in data.items():
            min_value = min(destinations.values(), default=999)
            if min_value <= threshold:
                file.write(f"{source} -> {min(destinations, key=destinations.get, default=999)}: {min_value}\n")
                for dest, value in destinations.items():
                    if value == min_value:
                        file.write(f"{source} -> {dest}: {value}\n")

# Set the threshold for minimum values
threshold_value = 60

# Call the function with your airport_data and threshold
find_minimum_values(adjacency_list, threshold_value)



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