# def kbc():
name=input("enter the name:")
print("welcome to KBC game")
question=["1)How many continents are there?","2)What is the capital of India?","3)NG mei kaun se course padhaya jaata hai?","4)whats is the capital of karnataka"]
options=[["a)Four", "b)Nine", "c)Seven", "d)Eight"],
         ["a)Chandigarh", "b)Bhopal", "c)Chennai", "d)Delhi"],
         ["a)Software Engineering", "b)Counseling", "c)Tourism", "d)Agriculture"],
         ["a)chennai","b)bangalore","c)mangalore","d)hydrabad"]]
help_line=[["a)four","b)seven"],["a)Chennai", "b)Delhi"],["a)Software Engineering", "b)Counseling"],["a)bangalore","b)mangalore"]]
ans=["c","d","a","b"]
helpline_ans=["b","b","a","a"]
price_distrubution=["CONGRULATION YOU WIN THE 10000$","SUPERB YOUR ANSWER IS CORRECT 15000$","CONGRULATION YOU WON 20000$","WONDERFUL ANSWER!YOU CORRECT 25000"]
i=0
count=0
def fifty(i):
    global count
    if count==0:
        count+=1
        k=0
        while k<len(help_line[i]):
            print(help_line[i][k])
            k=k+1
        choice=input("enter your answer")
        if choice==helpline_ans[i]:
            return True
        else:
            return False
def answer(i):
    print("5050")
    choice=input("enter your answer")
    if choice=="5050":
        return fifty(i)
    else:
        return False
def question():
    i=0
    while i<len(question):
        print(question[i])
        j=0
        while j<len(options[i]):
            print(options[i][j])
            j=j+1
        a=answer(i)
        if a==False:
            print("wrong answer")
            break
        elif a==True:
            print("congrulation",price_distrubution[i])
        i=i+1
fifty(i)
        
            