print("Kodlamaio")
baslik = "Taşit Kredisi"
print(baslik)
#string -> metinsel ifadeler
baslik = "İhtiyaç Kredisi"
print(baslik)
#int, integer -> tam sayı
vade = 36  # numeric ifade (int)
ekVade = 12
vade2 = "36" # metinsel ifade (str)

#float, decimal, double
AylikOdeme = 200.50

#bool, boolean -> True veya False
yukselisteMi = True

# matemetiksel operatörler

# +

print(5 + 5)
print(vade + 2)
print(vade + ekVade)
print(vade + ekVade)

# -

print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 12)

# *

print(5*5)
print(vade*2)
print(vade*ekVade)
print(36 * 12)

# /

print(5 / 5)
print(vade / 2)
print(vade / ekVade)
print(36 / 12)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % -> mod operatörü
print(10%2)
print(vade%5)
print(vade%ekVade)

# mantıksal operatörler
print(1 == 1)
print(1 == 2)

print(1 > 5)
print(7 > 3)
print(9 >= 9 )

print(4 < 2)
print(4 < 17)
print(3 <= 3)

print(1 != 1)
print(1 != 2)


# or, and


# or -> veya
print(1 > 2 or 5 > 2)


# and -> ve
print(1 > 2 and 5 > 2)


# karar yapıları
# if-elif-else

sayi1 = 10
sayi2 = 15


#indent -> girinti
if sayi1 > sayi2:
    print("Sayi 1 Sayi 2 den daha büyük")
else:
    print("Sayı 1 Sayı 2 den daha küçük")
