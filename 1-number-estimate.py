import random
sayi=random.randint(1,10)
count=0
girilen_deger=0
while True:
    girilen_deger=input("Lütfen Tahmininizi Giriniz: ")
    count += 1 
    if girilen_deger=="çık":
       print("Oyundan  Çıktınız.")
       break
    girilen_deger=int(girilen_deger)
    if girilen_deger > sayi:
        print("Lütfen Daha Küçük Bir Sayı Giriniz.")
    elif girilen_deger < sayi:
        print("Lütfen Daha Büyük Bir Sayı Giriniz.")
    else:
        print("Tebrikler! Doğru Tahmin Ettiniz.")
        print("Kullandığınız Hak Sayısı: ", count)
        break