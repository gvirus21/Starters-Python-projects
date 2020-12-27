import random
randNum=random.randint(0,100)
attempts=0
level=input("Enter your difficulty (e,m or h):")
#print(f"#Your Number {randNum}")#hide

def compare(randNum):
    userNum=int(input("Enter your number :"))
    if userNum>randNum :
        feedback=2
        output="guess is high"
    elif userNum<randNum:
        feedback=0
        output="guess is low"
    else :
        feedback=1
        output="congrats!! you got it"
    return feedback,output

def difficulty(level):
    if level=="e":
        attempts=10
        diff(attempts)
    elif level=="m":
        attempts=7
        diff(attempts)
    elif level=="h":
        attempts=5
        diff(attempts)
        
def diff(attempts):
    for i in range (0,attempts):
        print(f"{attempts-i} attempts left!")
        feedback,output=compare(randNum)
        if feedback==2:
            print(output)
        elif feedback==0:
            print(output)
        elif feedback==1:
            print(output)
            quit()
    print("Out of attempts!")
    quit()

difficulty(level)










    



