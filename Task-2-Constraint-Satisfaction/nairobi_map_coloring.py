import networkx as nx
import matplotlib.pyplot as plt

# Available colors
colors = ["red", "green", "blue", "yellow"]

# Simplified Nairobi sub-county adjacency graph
regions = {
    "Westlands": ["Dagoretti North", "Starehe"],
    "Dagoretti North": ["Westlands", "Dagoretti South"],
    "Dagoretti South": ["Dagoretti North", "Langata"],
    "Langata": ["Dagoretti South", "Kibra"],
    "Kibra": ["Langata", "Starehe"],
    "Starehe": ["Westlands", "Kibra", "Kamukunji"],
    "Kamukunji": ["Starehe", "Makadara"],
    "Makadara": ["Kamukunji", "Embakasi Central"],
    "Embakasi Central": ["Makadara", "Embakasi East"],
    "Embakasi East": ["Embakasi Central", "Embakasi North"],
    "Embakasi North": ["Embakasi East", "Ruaraka"],
    "Ruaraka": ["Embakasi North", "Mathare"],
    "Mathare": ["Ruaraka", "Kasarani"],
    "Kasarani": ["Mathare", "Roysambu"],
    "Roysambu": ["Kasarani", "Westlands"],
    "Embakasi South": ["Embakasi Central"],
    "Embakasi West": ["Embakasi Central"]
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
plt.figure(figsize=(14, 10))

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=2500,
    font_size=8,
    font_color='white'
)

plt.title("Nairobi Sub-County Map Coloring CSP")
plt.show()
