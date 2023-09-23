result = []
passenger = 0
for i in range(10):
    minus, plus = map(int, input().split())
    passenger = passenger - minus + plus
    result.append(passenger)

print(max(result))