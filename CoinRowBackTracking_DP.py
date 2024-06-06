def max_coin_row(coins):
    if len(coins) == 0:
        return 0, []

    if len(coins) == 1:
        return coins[0], [0]

    dp = [0] * len(coins)
    dp[0] = coins[0]
    dp[1] = max(coins[0], coins[1])

    selected_coins = [0] * len(coins)
    if coins[0] > coins[1]:
        selected_coins[0] = 1
    else:
        selected_coins[1] = 1

    for i in range(2, len(coins)):
        if dp[i - 1] > dp[i - 2] + coins[i]:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 2] + coins[i]
            selected_coins[i] = 1
        
        print("Iterasyon", i)
        print("DP:", dp)
        print("Seçilen coinler:", selected_coins)

    max_sum = dp[-1]
    selected = []
    i = len(coins) - 1
    while i >= 0:
        if selected_coins[i] == 1:
            selected.append(coins[i])
            i -= 2
        else:
            i -= 1

    return max_sum, selected[::-1]

# Örnek kullanım
coins = [1, 22, 3, 1,2,5,3,8,4,32,8,2,5,3,8,34,2,6,8,134,5,7,2]
max_sum, selected_coins = max_coin_row(coins)
print("En büyük toplam:", max_sum)
print("Seçilen coinler:", selected_coins)
