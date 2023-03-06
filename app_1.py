# Z modulu decimal dolacz typ Decimal
from decimal import Decimal

# snake case
user_age = 21
print(user_age)

# ctrl + shift + F10

# todo Typowanie dynamiczne
username = 'krzysiek'  # username okresla typ na podstawie tego co przypiszesz
# Kiedy program juz dziala mozesz zmienic typ zmniennej przypisac dana innego
# rodzaju

print(username.upper())

username = 100
print(username + 10)

# Numbers

x1 = 10    # liczby calkowite
# W Python liczby calkowite maja nieograniczony* rozmiar
x2 = 127836123781236836378123612783612273816317836127836127836127836127836127836
print(x2)

x3 = 14
x4 = 3
print(x3 + x4)
print(x3 - x4)
print(x3 * x4)
print(x3 ** x4)  # podnosisz x3 do potegi x4
print(x3 / x4)   # dzielenie rzeczywiste
print(x3 // x4)  # dzielenie calkowitoliczbowe (zawsze wynik zaokragla w dol)
print(x3 % x4)   # dzielenie zreszta (% czytasz MODULO)
print(x3 % 2)

# System binarny, szesnastkowy, osemkowy
x4 = 0b_100011010101
x5 = 0x_aaf
x6 = 0o_235

# Operacje bitowe

x7 = 12.3  # liczby zmiennoprzecinkowe
# Dlaczego zmiennoprzecinkowe
# 12.3 -> 123.0 * 10 ** -1
# 12.3 -> 1.23 * 10 ** 1
print(x7)

x8 = 0.1
x9 = 0.2
x10 = x8 + x9
print(x10)

# 12 -> 1100
# 0.3 ==> 0.0_1001_1001_1001_1001...
# https://www.rapidtables.com/convert/number/decimal-to-binary.html

# Tylko liczby ktore sa kombinacja potegi 2 jestes w stanie przechowac w sposob skonczony
# 0.75 = 0.25 + 0.5 = 2 ** -2 + 2 ** -1 = 0.11

# Pokazemy typ, ktory pozwala dokladnie przechowac liczby po przecinku
# Decimal
d1 = Decimal(12.3)  # jezeli tak napiszesz 12.3 to ta wartosc jest najpierw interpretowana
# jako floating-point, wiec jest przechowana w ten sposob w pamieci, traci dokladnosc i potem'
# dopiero konwertujesz na Decimal
# Jednym ze sposobow jest zapisanie wartosci w '' lub w ""
print(d1)

d2 = Decimal('12.3')
print(d2)

d3 = Decimal('13.6')
print(d3)

# Przeladowanie operatorow
d4 = d2 + d3
d5 = d2 - d3
d6 = d2 * d3

print(d4)
print(d5)
print(d6)

