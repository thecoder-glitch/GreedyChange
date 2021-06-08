#DPChange problem
data_open = open('/Users/taraghazanfari/Desktop/Week4_BENG181/dataset.txt', 'r')
data_read = data_open.read().splitlines()
money = int(data_read[0])
coins = []
for i in data_read[1].split(','):
    coins.append(int(i))



def DPChange(money, coins):
    MinNumCoins = [0]
    for m in range(1, money + 1):
        minNum = float('inf')
        for i in range(0, len(coins)):
            if m >= coins[i]:
                if MinNumCoins[m - coins[i]] + 1 < minNum:
                    minNum = MinNumCoins[m - coins[i]] + 1
        MinNumCoins.append(minNum)
    return MinNumCoins[money]


print(DPChange(money, coins))