import random
import time
import os


def cikisgerisayim(t):
    while t > 0:
        time.sleep(1)
        t -= 1
t = 3


def kelimeGosterimSuresi(k):
    while k > 0:
        time.sleep(1)
        k -= 1
k = 2


skor = 0
geciciskor = 0

kelimeler = ["kitaplık", "oyun", "masa", "mutfak", "araba", "otomobil", "Hız sınırı", "Güneş", "klayve", "bilgisayar", "youtube", "instagram", "kahverengi", "turkuaz", "mavi", "kırmızı", "mor", "yeşil", "sarı", "turuncu",
             "yazılım", "dolar", "ödev", "salon", "lavabo", "laboratuvar", "takım elbise", "battaniye", "yatak", "şeker", "seksendört", "emre", "çağan", "yunus", "kolpa", "müzik", "gitar", "radyo", "televizyon", "laptop",
             "java", "python", "html", "hiphop", "pop", "kpop", "başlat", "devam", "bitir"]
anaMenu = """
    Hafıza Oyunu
    
    1- Başla
    2- Skor
    3- Kurallar
    4- Çıkış
"""

while True:
    os.system("cls")
    print(anaMenu)
    anaMenu_secim = int(input("Seçiminiz -> "))
    #--------------------------------------------------------------------------------------------------------------------------
    if anaMenu_secim == 4:                                                                                              # Exit section
        os.system("cls")                                                                                                # Çıkış bölümü
        print("Çıkış yapılıyor...")
        print(cikisgerisayim(t))
        quit()
    #----------------------------------------------------------------------------------------------------------------------------
    elif anaMenu_secim == 3:                                                                                            # Rules section
        os.system("cls")                                                                                                # Kurallar bölümü
        print("-Kurallar-")
        print("1- Her kelime için görüş süresi 2 saniyedir.")
        print("2- Her doğru kelime için +2, her yanlış kelime için -1 puan alırsınız.")
        print("3- Kelimeleri yazmak için süre sınırı bulunmamaktadır.")
        print("4- Toplam 5 adet kelime gösterilecektir.")
        print("6- Kelimeleri tam gördüğünüz şekilde yazmanız gerekmektedir.")
        print()
        input("Devam etmek için enter'ı tuşlayınız.")
    #----------------------------------------------------------------------------------------------------------------------------
    elif anaMenu_secim == 1:                                                                                            # We ask the user to press enter so that the game does not start immediately after the user's selection.
        os.system("cls")                                                                                                # Kullanıcının seçiminden sonra oyunun hemen başlamaması için kullanıcıdan enter'ı tuşlamasını istiyoruz.
        input("Süreyi başlatıp kelimeleri görmek için enter'ı tuşlayınız.")
        os.system("cls")
        #--------------------------------------------------------------------------------------------------------------------------
        birinciKelime = random.choice(kelimeler)                                                                        # We choose a random word from the list called "kelimeler" above and print it on the screen for 2 seconds. We repeat this for 5 words.
        print(birinciKelime)                                                                                            # Yukarı listeden rastgele kelime seçtiriyor ve 2 saniye boyunca ekrana yazdırıyoruz. Bunu 5 kelime için tekrarlıyoruz.
        kelimeler.remove(birinciKelime)
        print(kelimeGosterimSuresi(k))
        os.system("cls")
        ikinciKelime = random.choice(kelimeler)
        print(ikinciKelime)
        kelimeler.remove(ikinciKelime)
        print(kelimeGosterimSuresi(k))
        os.system("cls")
        ucuncuKelime = random.choice(kelimeler)
        print(ucuncuKelime)
        kelimeler.remove(ucuncuKelime)
        print(kelimeGosterimSuresi(k))
        os.system("cls")
        dorduncuKelime = random.choice(kelimeler)
        print(dorduncuKelime)
        kelimeler.remove(dorduncuKelime)
        print(kelimeGosterimSuresi(k))
        os.system("cls")
        besinciKelime = random.choice(kelimeler)
        print(besinciKelime)
        kelimeler.remove(besinciKelime)
        print(kelimeGosterimSuresi(k))
        os.system("cls")
        #-----------------------------------------------------------------------------------------------------------------------
        print("Şimdi gördüğün kelimeleri yaz!")                                                                         # Here we ask the user to enter the words s/he sees.
        birinciKelimeGirdi = input("1- ")                                                                               # Burada kullanıcıdan gördüğü kelimeleri girmesini istiyoruz.
        ikinciKelimeGirdi = input("2- ")
        ucuncuKelimeGirdi = input("3- ")
        dorduncuKelimeGirdi = input("4- ")
        besinciKelimeGirdi = input("5- ")
        #-----------------------------------------------------------------------------------------------------------------------
        if birinciKelimeGirdi == birinciKelime:                                                                         # Here we add +2 points if the answer is correct and -1 point if incorrect. Where there is a def,
            skor = skor + 2                                                                                             # we control the answers written by the user to print them on the screen.
            geciciskor = geciciskor + 2                                                                                 # Burada eğer cevap doğru ise +2, yanlış ise -1 puan ekliyoruz. Fonksiyon olan yerlerde ise
        else:                                                                                                           # kullanıcının yazdıkları cevapları ekrana yazdırmak için kontrol ediyoruz
            skor = skor - 1
            geciciskor = geciciskor - 1
        def kelimeBirKontrol():
            if birinciKelimeGirdi == birinciKelime:
                print("Birinci kelimeniz doğru!")
            else: print("Birinci kelime '{}' olmalıydı. Sizin cevabınız '{}'".format(birinciKelime, birinciKelimeGirdi))
        if ikinciKelimeGirdi == ikinciKelime:
            skor = skor + 2
            geciciskor = geciciskor + 2
        else:
            skor = skor - 1
            geciciskor = geciciskor - 1
        def kelimeIkiKontrol():
            if ikinciKelimeGirdi == ikinciKelime:
                print("İkinci kelimeniz doğru!")
            else: print("İkinci kelime '{}' olmalıydı. Sizin cevabınız '{}'".format(ikinciKelime, ikinciKelimeGirdi))
        if ucuncuKelimeGirdi == ucuncuKelime:
            skor = skor + 2
            geciciskor = geciciskor + 2
        else:
            skor = skor - 1
            geciciskor = geciciskor - 1
        def kelimeUcKontrol():
            if ucuncuKelimeGirdi == ucuncuKelime:
                print("Üçüncü kelimeniz doğru!")
            else: print("Üçüncü kelime '{}' olmalıydı. Sizin cevabınız '{}'".format(ucuncuKelime, ucuncuKelimeGirdi))
        if dorduncuKelimeGirdi == dorduncuKelime:
            skor = skor + 2
            geciciskor = geciciskor + 2
        else:
            skor = skor - 1
            geciciskor = geciciskor - 1
        def kelimeDortKontrol():
            if dorduncuKelimeGirdi == dorduncuKelime:
                print("Dördüncü kelimeniz doğru!")
            else: print("Dördüncü kelime '{}' olmalıydı. Sizin cevabınız '{}'".format(dorduncuKelime, dorduncuKelimeGirdi))
        if besinciKelimeGirdi == besinciKelime:
            skor = skor + 2
            geciciskor = geciciskor + 2
        else:
            skor = skor - 1
            geciciskor = geciciskor - 1
        def kelimeBesKontrol():
            if besinciKelimeGirdi == besinciKelime:
                print("Beşinci kelimeniz doğru!")
            else: print("Beşinci kelime '{}' olmalıydı. Sizin cevabınız '{}'".format(besinciKelime, besinciKelimeGirdi))
        #------------------------------------------------------------------------------------------------------------------------
        input("Sonucunuzu görmek için enter'ı tuşlayınız.")                                                             # Checking the words entered by the user and print them on the screen.
        print(kelimeBirKontrol())                                                                                       # Re-adding words to our list that we have deleted before.
        print(kelimeIkiKontrol())                                                                                       # Kullanıcının girdiği kelimeleri kontrol ediyor ve ekrana yazdırıyoruz.
        print(kelimeUcKontrol())                                                                                        # Daha öncesinde silmiş olduğumuz kelimeleri geri listemize ekliyoruz
        print(kelimeDortKontrol())
        print(kelimeBesKontrol())
        kelimeler.append(birinciKelime)
        kelimeler.append(ikinciKelime)
        kelimeler.append(ucuncuKelime)
        kelimeler.append(dorduncuKelime)
        kelimeler.append(besinciKelime)
        print("Skorunuz: ", geciciskor)
        input("Devam etmek için enter'ı tuşlayınız.")
        geciciskor = 0
        #-----------------------------------------------------------------------------------------------------------------------
    elif anaMenu_secim == 2:                                                                                            # Print our total score on the screen.
        os.system("cls")                                                                                                # Toplam skorumuzu ekrana yazdırıyoruz.
        print("Toplam skorunuz: ", skor)
        input("Devam etmek için enter'ı tuşlayınız.")
