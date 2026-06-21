binary = 1011
decimal = 0
power = 0
while binary > 0:
    digit = binary % 10
    decimal += digit * (2 ** power)
    power += 1
    binary //= 10
print(decimal)

