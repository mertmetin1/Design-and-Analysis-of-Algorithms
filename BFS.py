from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


def bfs(start_node):
    # Kuyruk oluştur ve başlangıç düğümünü kuyruğa ekle
    queue = deque([start_node])
    start_node.visited = True
    
    # BFS gezinmesi
    while queue:
        current_node = queue.popleft()
        print(current_node.value, end=" ")  # Düğüm değerini yazdır
        
        # Düğümün komşularını işaretle ve kuyruğa ekle
        for neighbor in current_node.neighbors:
            if not neighbor.visited:
                neighbor.visited = True
                queue.append(neighbor)


# Grafı oluştur
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.add_neighbor(node2)
node1.add_neighbor(node3)
node2.add_neighbor(node4)
node3.add_neighbor(node5)

# BFS gezinmesini başlat
print("BFS gezinmesi:")
bfs(node1)
