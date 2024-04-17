import itertools

import numpy as np

def brute_force_assignment(cost_matrix):
    min_cost = float('inf')
    best_assignment = None
    
    num_agents, num_tasks = cost_matrix.shape
    
    # Tüm olası atamaların kombinasyonlarını oluştur
    all_assignments = itertools.permutations(range(num_tasks))
    # Her kombinasyon için toplam maliyeti hesapla ve en iyisini güncelle
    for assignment in all_assignments:
        print(assignment)
        total_cost = sum(cost_matrix[i][assignment[i]] for i in range(num_agents))
        
        if total_cost < min_cost:
            min_cost = total_cost
            best_assignment = assignment
            
    return best_assignment

# Örnek kullanım:
cost_matrix = np.array([[10, 19, 8, 15],
                        [10, 18, 7, 17],
                        [13, 16, 9, 14],
                        [12, 19, 8, 18]])

optimal_assignment = brute_force_assignment(cost_matrix)
print("Optimal Assignment:")
print(optimal_assignment)
