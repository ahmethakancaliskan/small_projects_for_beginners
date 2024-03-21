
print("Kırıkkale Üniversitesi Harf Notu ve Ortalama Hesaplama Uygulamasına Hoşgeldiniz.")
while True:

    ort = 0
    vize_yuzdesi = 60
    final_yuzdesi = 40
    vize_sonucu = int(input('  Vize Sonucunuzu Giriniz..: '))
    final_sonucu = int(input('  Final Sonucunuzu Giriniz..: '))
    ort =  vize_sonucu*(vize_yuzdesi/100) + final_sonucu*(final_yuzdesi/100)
    print(" Dönem Sonu Ortalamanız : ",ort)

    if ort >= 88:
        print('  Harf Notunuz : AA'+' (Mükemmel)')
    elif ort >=81 and ort <=87:
        print('  Harf Notunuz : BA'+' (Çok İyi)')
    elif ort >=74 and ort <=80:
        print('  Harf Notunuz : BB'+' (İyi)')
    elif ort >=67 and ort <=73:
        print('  Harf Notunuz : CB' +' (Orta)')
    elif ort >=60 and ort <=66:
        print('  Harf Notunuz : CC'+' (Geçer)')
    elif ort >=53 and ort <=59:
        print('  Harf Notunuz : DC'+' (Koşullu Geçer)')
    elif ort >=46 and ort <=52:
        print('  Harf Notunuz : DD'+' (Koşullu Geçer)')
    elif ort >=39 and ort <=45:
        print('  Harf Notunuz : FD'+' (Başarısız Oldunuz)')
    else:
        print('  Harf Notunuz : FF'+' (Başarısız Oldunuz)')

    devam = input("Yeni hesaplama yapmak istiyor musunuz? (Evet için 'E', Hayır için 'H'): ")
    
    if devam.upper() != 'E':
        print("Program kapatılıyor...")
        break
input() 