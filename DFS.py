class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False  # Ziyaret edildi mi? bilgisini tutmak için

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


def dfs(node):
    if node is None: # bu ne aq
        return
    
    # Düğümü ziyaret et
    node.visited = True
    print(node.value, end=" ")

    # Düğümün komşularını ziyaret et
    for neighbor in node.neighbors:
        if not neighbor.visited:
            dfs(neighbor)

def dfs_recursive(node):
    if node.visited:
        return
    
    node.visited = True
    print(node.value, end=" ")
    
    for neighbor in node.neighbors:
        dfs_recursive(neighbor)

# Grafı oluşturalım
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.add_neighbor(node2)
node1.add_neighbor(node3)
node2.add_neighbor(node4)
node3.add_neighbor(node5)
node3.add_neighbor(node1)


# DFS gezinmesini başlatıyoruz
print("DFS gezinmesi:")
dfs(node1)
