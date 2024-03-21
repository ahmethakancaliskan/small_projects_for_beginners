
print("Welcome to The Lottery Game! Good Luck!")
while True:

    winning_numbers = ['1','6','0','6','9','9'] # kazanan sayılar
    your_prediction = [] # list of your predicts

    for para in range(6):
        entered_numbers = input('Enter a number for play..: ')   # give your number 6 times
        your_prediction.append(entered_numbers) # this method is adding your numbers into the your predict's list
        
    if winning_numbers == your_prediction:    # winning
        print('.......Congratulations, You Won the Jackpot.......') #Tebrikler Büyük İkramiyeyi Kazandınız
        print(f'Jackpot Number : {winning_numbers} \n Your Prediction : {your_prediction} ')
    else:
        print('Please try again')
        print("Want to Try Again? ('Y' for Yes', 'N' for No)")
    
    tekrarDene = input('')
    if tekrarDene.upper() != 'Y':
        print("....GameOver....")
        break
    
input()

