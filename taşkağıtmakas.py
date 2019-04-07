import random #burada random modülünü dahil ettik
puan_oyuncu = 0
puan_bilgisayar = 0  #2 adet değişken atadık
print("Çıkmak için 0'a basın.")
while (True): #döngü başlattık
  print("Taş=1\nKağıt=2\nMakas=3")
  oyuncu = int(input("Seçiminizi yapın:"))
  bilgisayar = random.randint(1, 3) #bilgisayarın rastgele seçim yapmasını istedik
  if (oyuncu == bilgisayar):
    print("Berabare")
    print("")
  elif (oyuncu == 0):
    break
  elif (oyuncu == 1 and bilgisayar == 2):
    puan_bilgisayar = puan_bilgisayar + 1 #sayaç başlattık ve diğerlerinde de
    print("Bilgisayarın seçimi:",bilgisayar)
    print("Bilgisayar 1 puan aldı.")
    print("Oyuncu:",puan_oyuncu,"Bilgisayar",puan_bilgisayar)
    print("")
  elif (oyuncu == 1 and bilgisayar == 3):
    puan_oyuncu = puan_oyuncu + 1
    print("Bilgisayarın seçimi:",bilgisayar)
    print("Oyuncu 1 puan aldı.")
    print("Oyuncu:",puan_oyuncu,"Bilgisayar",puan_bilgisayar)
    print("")
  elif (oyuncu == 2 and bilgisayar == 1):
    puan_oyuncu = puan_oyuncu + 1
    print("Bilgisayarın seçimi:",bilgisayar)
    print("Oyuncu 1 puan aldı.")
    print("Oyuncu:",puan_oyuncu,"Bilgisayar",puan_bilgisayar)
    print("")
  elif (oyuncu == 2 and bilgisayar == 3):
    puan_bilgisayar = puan_bilgisayar + 1
    print("Bilgisayarın seçimi:",bilgisayar)
    print("Bilgisayar 1 puan aldı.")
    print("Oyuncu:",puan_oyuncu,"Bilgisayar",puan_bilgisayar)
    print("")
  elif (oyuncu == 3 and bilgisayar == 1):
    puan_bilgisayar = puan_bilgisayar + 1
    print("Bilgisayarın seçimi:",bilgisayar)
    print("Bilgisayar 1 puan aldı.")
    print("Oyuncu:",puan_oyuncu,"Bilgisayar",puan_bilgisayar)
    print("")
  elif (oyuncu == 3 and bilgisayar == 2):
    puan_oyuncu = puan_oyuncu + 1
    print("Bilgisayarın seçimi:",bilgisayar)
    print("Oyuncu 1 puan aldı.")
    print("Oyuncu:",puan_oyuncu,"Bilgisayar",puan_bilgisayar)
    print("")
