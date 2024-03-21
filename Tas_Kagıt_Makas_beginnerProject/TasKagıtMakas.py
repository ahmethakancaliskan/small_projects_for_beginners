import random  # random modülünü import etme
print("TAŞ-KAĞIT-MAKAS OYUNUNA HOŞGELDİNİZ!")
adınız = input('Adınızı Giriniz..: ').upper()

skorRobot = 0
skorUser = 0
while True:
    
    oyun = ['Taş','Kağıt','Makas']
    oyuncuRobot = random.choice(oyun)   # random modülünün fonksiyou ile 'oyun' adlı listeden rastgele eleman seçimi
    
    user = input('Taş ? Kağıt? Makas? ').capitalize()  # kullanıcının yazdığı kelimenin baş harfini büyütme fonksiyonu
    

    if oyuncuRobot == 'Taş' and user == 'Makas':
        skorRobot+= 1
        print('\n ROBOT: ',oyuncuRobot,' ', adınız,': ',user)
        print('BU RAUNDU KAZANAN ROBOT !!')
        print('SKOR= ROBOT: ',skorRobot,' ', adınız, ':', ' ', skorUser)
        print('\n')
    

    elif oyuncuRobot == 'Makas' and user == 'Kağıt':
        skorRobot+= 1
        print('\n ROBOT: ',oyuncuRobot,' ', adınız,': ',user)
        print('SKOR= ROBOT: ',skorRobot,' ', adınız, ':', ' ', skorUser)
        print('\n')
    
    
    elif oyuncuRobot == 'Kağıt' and user == 'Taş':
        skorRobot+= 1
        print('\n ROBOT: ',oyuncuRobot,' ', adınız,': ',user)
        print('SKOR= ROBOT: ',skorRobot,' ', adınız, ':', ' ', skorUser)
        print('\n')
    
    
    elif oyuncuRobot == user:
        print('\n Tekrar!!')
        print('\n ROBOT: ',oyuncuRobot,' ', adınız,': ',user)
        print('SKOR= ROBOT: ',skorRobot,' ', adınız, ':', ' ', skorUser)
        print('\n')
    
    else:
        skorUser+= 1
        print('\n ROBOT: ',oyuncuRobot,' ', adınız,': ',user)
        print('BU RAUNDU KAZANAN',adınız)
        print('SKOR= ROBOT: ',skorRobot,' ', adınız, ':', ' ', skorUser)
        print('\n')
    
    if skorRobot  == 3:
        print('\n OYUNU KAZANAN : ROBOT!!')
        print('SONUÇ= ROBOT: ',skorRobot,' ',adınız,':',' ',skorUser)
        print("\n TEKRAR OYNAMAK İÇİN E OYUNDAN ÇIKMAK İÇİN HERHANGİ BİR TUŞA BASIN.")
        devam = input('').upper()
        if devam != 'E':
            print('______GÜLE GÜLE',adınız,'______')
            input()
            break
            
        else:
            skorUser = 0
            skorRobot = 0
        
    if skorUser == 3:
        print('\n OYUNU KAZANAN : ',adınız,'!!' )
        print('SONUÇ= ROBOT: ',skorRobot,' ',adınız,':',' ',skorUser)
        print("\n  TEKRAR OYNAMAK İÇİN E OYUNDAN ÇIKMAK İÇİN HERHANGİ BİR TUŞA BASIN.")
        
        devam = input('').upper()
        if devam != 'E':
            print('______GÜLE GÜLE',adınız,'______')
            input()
            break
            
        else:
            skorUser = 0
            skorRobot = 0
    
        


    
