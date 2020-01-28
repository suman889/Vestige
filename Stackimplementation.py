
        
        #Queu implementation in Python
def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False

def Push(stk, item):
    stk.append(item)
    top=len(stk)-1

def Pop (stk):
    if isEmpty (stk):
        return "Underflow"
    else:
        item=stk.pop()
        if len(stk) ==0:
            top=None
        else:
            
            top=len(stk)-1
        return item


def Peek (stk):
    if isEmpty(stk):
        return "Underflow"

    else:
        top=len(stk)-1
        return stk[top]


def disp(stk):
    if isEmpty(stk):
        print("Stack Empty")

    else:
        top =len(stk)-1
        print(stk[top],"<- top")
        for a in range(top-1,-1,-1):
            print(stk[a])

stack=[]

top= None
while True:
    print('\n\nStack Operations:')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Display Stack')
    print('5. Exit')
    ch=int(input("Enter your Choice : " ))
    if ch==1:
        item=int(input('Enter Item: '))
        Push(stack,item)
    elif ch==2:
        item=Pop(stack)
        if item=='Underflow':
            print('stack is Empty')

        else:
            print('Popped item is :',item)
    elif ch==3:
        item=Peek(stack)
        if item=='Underflow':
            print('Stack is empty')

        else:
            print('Topmost item is  :', item)
    elif ch==4:
        disp(stack)
    elif ch==5:
        break
    else:
        print('Invalid choice')

            
            
        
