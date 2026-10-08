# # Objecitve write ewma(prices, lam)

# def ewma(prices, lam):
#     out = []
#     run = prices[0]
#     out.append(run)
#     for p in prices[1:]:
#         run = lam * run + (1 - lam) * p
#         out.append(run)
#     return out

# test_prices = [55, 99, 100, 24]
# lam = 0.5

# print(ewma(test_prices, lam))
import random
def simulate_coin_game(n, trials):
    wins = 0
    for _ in range (trials):
        a_heads = sum(random.randint(0,1) for _ in range(n + 1))
        b_heads = sum(random.randint(0,1) for _ in range(n))
        if a_heads > b_heads:
            wins += 1
    return wins / trials

print(simulate_coin_game(n=500, trials=100000))



