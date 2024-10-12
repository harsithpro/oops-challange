import random
class fruit:
    def __init__(self):
        self.fruit={'apple':'red','banana':'yellow','mango':'yellow','orange':'orange'}
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruit.items()))
            print("quelle est le couleur de {}".format(fruit))
            user=input()
            if(user.lower()==color):
                print("correct answer")
            else:
                print("wrong answer")
            option=int(input("enter 0 if u want to play again or enter uno numero u idioto"))
            if option:
                break
print("welcome to fruit quiz")
ob=fruit()
ob.quiz()