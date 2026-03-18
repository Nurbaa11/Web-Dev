total_sum = 0

for _ in range(100):
    try:
        number = int(input())
        total_sum += number
    except EOFError:
        break

print(total_sum)