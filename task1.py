binary = 1011
decimal = 0
power = 0
while binary > 0:
    digit = binary % 10
    decimal += digit * (2 ** power)
    power += 1
    binary //= 10
print(decimal)


#ippudu oka sample folder teeskunnam
#dantlo oka task1.py file vesam
#ardam aindaha

# ardham ayindhi
#2. Ippudu terminal open cheyyali
#ippudu same neelane osthundi choodu
#ippudu malli save cheyyali