import networkx as nx
import matplotlib.pyplot as plt

stations = ["Lionel-Groulx", "Lucien-L'Allier", "Bonaventure",
            "Square-Victoria-OACI", "Place-d’Armes", "Champ-de-Mars",
            "Berri-UQAM", "Sherbrooke", "Mont-Royal", "Beaudry", "Guy-Concordia",
            "Peel", "McGill", "Place-des-Arts", "Saint-Laurent", "Vendôme", "Place-Saint-Henri"]

edges = [("Lionel-Groulx", "Place-Saint-Henri", 0.8),
         ("Place-Saint-Henri", "Vendôme", 0.7),
         ("Lionel-Groulx", "Lucien-L'Allier", 1.0),
         ("Lucien-L'Allier", "Bonaventure", 0.8),
         ("Bonaventure", "Square-Victoria-OACI", 0.7),
         ("Square-Victoria-OACI", "Place-d’Armes", 0.9),
         ("Place-d’Armes", "Champ-de-Mars", 0.6),
         ("Champ-de-Mars", "Berri-UQAM", 1.0),
         ("Berri-UQAM", "Sherbrooke", 0.9),
         ("Sherbrooke", "Mont-Royal", 0.7),
         ("Berri-UQAM", "Beaudry", 0.8),
         ("Lionel-Groulx", "Guy-Concordia", 0.5),
         ("Guy-Concordia", "Peel", 0.7),
         ("Peel", "McGill", 0.8),
         ("McGill", "Place-des-Arts", 0.7),
         ("Place-des-Arts", "Saint-Laurent", 0.6),
         ("Saint-Laurent", "Berri-UQAM", 0.8)]

if __name__ == "__main__":
 G = nx.Graph()
 G.add_nodes_from(stations)

# додаємо ребра з вагами
 for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Аналіз
 num_nodes = G.number_of_nodes()
 num_edges = G.number_of_edges()
 degrees = dict(G.degree())

# Вивід у консоль (опціонально)
 print("Кількість станцій (вузлів):", num_nodes)
 print("Кількість сполучень (ребер):", num_edges)
 print("\nСтупінь станцій:")
 for node, degree in degrees.items():
     print(f"{node}: {degree}")

 plt.figure(figsize=(15, 15))
 plt.title("Часткова карта метро Montréal")

 pos = nx.spring_layout(G, seed=42, k=0.3)
 nx.draw(G, pos, with_labels=True, node_size=1100, node_color="lightblue", font_size=7, font_weight="bold")
 nx.draw_networkx_edges(G, pos, width=1, edge_color="gray")

 edge_labels = nx.get_edge_attributes(G, "weight")
 nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green', label_pos=0.5, rotate=False)

# Додати інформацію про граф у правий верхній кут
 graph_info = f"Кількість станцій (вузлів): {num_nodes}\nКількість сполучень (ребер): {num_edges}\n\nСтупінь станцій:\n"
 for node, degree in degrees.items():
     graph_info += f"{node}: {degree}\n"

 plt.text(0.02, 0.7, graph_info, fontsize=10, va='center', ha='left', transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.7))
 plt.axis('off')

 plt.show()
