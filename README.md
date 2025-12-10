Порівняння DFS та BFS у графі метро Montréal

Для стартової вершини Berri-UQAM алгоритми формують різні шляхи:

DFS (Depth-First Search)

DFS заглиблюється у граф, переходячи до першого доступного сусіда та продовжує шлях максимально глибоко.
Тому шлях є схожим на довгу “гілку дерева”. Порядок обходу залежить від того, у якому порядку записані суміжні вершини.

DFS шлях:
Berri-UQAM -> Champ-de-Mars -> Place-d’Armes -> Square-Victoria-OACI -> Bonaventure -> Lucien-L'Allier -> Lionel-Groulx -> Place-Saint-Henri -> Vendôme -> Guy-Concordia -> Peel -> McGill -> Place-des-Arts -> Saint-Laurent -> Sherbrooke -> Mont-Royal -> Beaudry

BFS (Breadth-First Search)

BFS працює пошарово: спочатку обходить всіх сусідів, потім сусідів сусідів.
Тому він спочатку знаходить усі вершини, які знаходяться на відстані 1 ребро, потім 2, потім 3.

BFS шлях:
Berri-UQAM -> Champ-de-Mars -> Sherbrooke -> Beaudry -> Saint-Laurent -> Place-d’Armes -> Mont-Royal -> Place-des-Arts -> Square-Victoria-OACI -> McGill -> Bonaventure -> Peel -> Lucien-L'Allier -> Guy-Concordia -> Lionel-Groulx -> Place-Saint-Henri -> Vendôme

Висновки:
DFS пріоритезує глибину, тому рухається від вузла до вузла, поки можливо.
BFS пріоритезує ширину, тому спочатку відвідує всі вершини на мінімальній відстані.