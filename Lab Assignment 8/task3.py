f = open("input3_1.txt", "r")
fo = open("output3.txt", "w")

def coinsCombo(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[target] != float('inf'):
      return dp[target]
    else:
      return -1

fl = f.readline().strip().split(" ")
n = int(fl[0])
target = int(fl[1])

coins = f.readline().strip().split(" ")
for i in range(len(coins)):
    coins[i]=int(coins[i])


ans = coinsCombo(coins, target)
fo.writelines(f"{ans}")

f.close()
fo.close()