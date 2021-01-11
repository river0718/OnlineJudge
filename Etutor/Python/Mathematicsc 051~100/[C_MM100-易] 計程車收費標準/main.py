total_money, K, M, total_km = map(int, input().split())

if total_km >= M:
    total_money = total_money + (total_km - M) * (K + 5) + M * K
else:
    total_money = total_money + K * total_km

print(total_money)
