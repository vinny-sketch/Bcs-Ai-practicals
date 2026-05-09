import networkx as nx
import matplotlib.pyplot as plt

# Available colors
colors = ["red", "green", "blue"]

# Australia regions and adjacency
regions = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

# Store assigned colors
color_assignment = {}

# Constraint checker
def is_valid(region, color):
    for neighbor in regions[region]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True

# Backtracking algorithm
def solve(region_list, index=0):
    if index == len(region_list):
        return True

    region = region_list[index]

    for color in colors:
        if is_valid(region, color):
            color_assignment[region] = color

            if solve(region_list, index + 1):
                return True

            del color_assignment[region]

    return False

# Solve CSP
region_list = list(regions.keys())
solve(region_list)

# Create graph
G = nx.Graph()

for region, neighbors in regions.items():
    for neighbor in neighbors:
        G.add_edge(region, neighbor)

# Node colors
node_colors = [color_assignment[node] for node in G.nodes()]

# Draw graph
plt.figure(figsize=(8, 6))

nx.draw(
    G,
    with_labels=True,
    node_color=node_colors,
    node_size=3000,
    font_size=10,
    font_color='white'
)

plt.title("Australia Map Coloring CSP")
plt.show()
