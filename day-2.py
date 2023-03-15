sistem = ["Muharrem Demirel","Ali Metin","Mehmet Pak"]    # Öğrenci isim ve  soy isimlerinin kaydedildigi sistem.
print(sistem)

print("")
print("")
print("**************************")

ekleme = input("İsim ve soyisim giriniz: ")  # Listeye öğrenci ekleme
sistem.append(ekleme)
print(sistem)
print("")

print("**************************")

silme = input("Silmek istediğiniz isim soyismi giriniz: ")  #Listeden öğrenci silme
sistem.remove(silme) 
print(sistem)
print("")
print("**************************")

CokluEkleme = []          #Listeye birden fazla isim ekleme
sor=int(input("Kaç isim eklemek istiyorsunuz: "))
for i in range(sor):
    n=input("Eklemek istediğiniz isimleri sıra ile giriniz: ")
    CokluEkleme.append(n)

sistem.extend(CokluEkleme)
print(sistem)
print("")
print("**************************")

a=0
while a < len(sistem):            #Listedeki isimleri yazdırma
    print(a+1,". isim:",sistem[a])
    a+=1

ara = input("Hangi öğrencinin numarasını öğrenmek istiyorsunuz? ")
for  j in range(len(sistem)):
    if ara == sistem[j]:
        print(ara,"isimli öğrencinin numarası :",j)
        
print("")
print("**************************")


sor=int(input("Kaç isim silmek istiyorsunuz: "))     # Listeki birden fazla ismi silme
for i in range(sor):
    isim=input("Silmek istediğiniz isim ? ")
    for j in sistem:
            if j == isim:
                sistem.remove(isim)

print(sistem)