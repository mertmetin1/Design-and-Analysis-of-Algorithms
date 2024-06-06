def alg(B):
    sq = 0
    for i in range(len(B)):
        r = 0
        for j in range(len(B)):
            if B[i][j] == 0 and B[i][j-1] == 0:
                r += 1
            elif B[i][j] == 1:
                break
        d = 0
        for k in range(r):
            for t in range(r):
                
                if i+k < len(B) and j+t < len(B[i+k]) and B[i+k][j+t] != 0:
                    d = -1
                else:
                    d = r
        if d > sq:
            sq = d
            
    return sq

big_matrix = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

result = alg(big_matrix)
print(result)