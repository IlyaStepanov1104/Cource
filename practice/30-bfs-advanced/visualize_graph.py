import math

import networkx as nx
import matplotlib.pyplot as plt
 
 
def visualize_graph(graph, directed=True, weighted=True, rad=0.05):
    """
    graph - словарь вида {key: [(key_2, w), ...]}
 
    directed - True, если рёбра односторонние
    weighted - True, если нужно подписать веса рёбер
    rad - изгиб дуги, тот же, что передаётся в connectionstyle
    """
    G = nx.DiGraph() if directed else nx.Graph()
 
    for node, edges in graph.items():
        G.add_node(node)
        for to, weight in edges:
            G.add_edge(node, to, weight=weight)
 
    pos = nx.spring_layout(G, seed=42)
 
    plt.figure(figsize=(6, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="#6699ff",
        node_size=800,
        font_color="white",
        font_size=12,
        arrows=directed,
        arrowsize=20,
        arrowstyle="-|>",
        connectionstyle=f"arc3,rad={rad}",
    )
 
    if weighted:
        # nx.draw_networkx_edge_labels ставит подпись в середину прямой
        # линии, не учитывая изгиб дуги. Если между двумя вершинами есть
        # рёбра в обе стороны, их подписи накладываются друг на друга.
        # Поэтому считаем позицию подписи так же, как изгибается дуга.
        for u, v, data in G.edges(data=True):
            x1, y1 = pos[u]
            x2, y2 = pos[v]
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
 
            dx, dy = x2 - x1, y2 - y1
            length = math.hypot(dx, dy)
            if length == 0:
                continue
 
            # перпендикуляр к ребру, смещение как у середины квадратичной кривой
            perp_x, perp_y = -dy / length, dx / length
            offset = 0.5 * rad * length
            lx, ly = mx + perp_x * offset, my + perp_y * offset
 
            plt.text(
                lx, ly, str(data["weight"]),
                fontsize=10, ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none"),
            )
 
    plt.show()


