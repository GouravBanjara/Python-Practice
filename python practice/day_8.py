# custom errors (raise keyword)
# a = int(input('Enter any value between 5 and 9'))
# if (a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9") #raising error 
# else:   
#     pass


# exercise 2 KBC game
questions = [['Which is the largest ocean in the world?','Atlantic','Indian','Arctic','Pacific',4],
            ['Which is the third largest planet in our solar system?','Earth','Jupiter','Uranus','Saturn',3],
            ['Which language was used to create facebook?','Java','C','Php','Python',3],
            ['Which is the most expensive production car in the world?','RR Boat Tail','Buggatti La Voiture Noire','RR Sweptail','Pagani Huyara Imola',1]]

levels = [1000,5000,10000,50000]
money  = 0
i = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f'Question {i+1} for Rs. {levels[i]}')
    print(f'{question[0]}')
    print(f'1.{question[1] }             2.{question[2]} ')
    print(f'3.{question[3]}              4.{question[4]} ')

    reply = int(input('Enter your answer (1-4):- '))
    if (reply ==question[-1]):
        print()
        print(f'Correct answer, you have won Rs.{levels[i]}')
        print()
        print()
    else:
        if (i>2):
            money = 10000
            print(f'Incorrect answer, You have been brought down to your last checkpoint and You won Rs.{money}')
        else:
            print('Incorrect answer, Good Luck next Time')
            break


