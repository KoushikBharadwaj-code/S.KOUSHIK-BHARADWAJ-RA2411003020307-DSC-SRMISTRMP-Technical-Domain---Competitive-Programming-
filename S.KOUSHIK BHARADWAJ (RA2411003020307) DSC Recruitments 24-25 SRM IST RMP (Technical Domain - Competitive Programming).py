                                                                                                                #DEVELOPER STUDENTS CLUB
                                                                                                                             #SRM IST RMP
                                                                                                #RECRUITMENTS 24-25  (TECHNICAL DOMAIN)
                                                                                                               #COMPETITIVE PROGRAMMING
#S.KOUSHIK BHARADWAJ
#RA2411003020307
#CSE CORE-'E'


#1.
'''def wordarrinsen(sen):
    words=sen.split()
    wordsort=sorted(words,key=len)
    return ' '.join(wordsort)
print(wordarrinsen("This is a cool sentence"))'''

#2.
'''a=[2,3,4,4,6,7,7]
for i in a:
    if a.count(i)>1:
        a.remove(i)
print(a)'''

#4.
'''s=6
m=12
l=24
xl=48
n=140
a=n//xl
n=n%xl
b=n//l
n=n%l
c=n//m
n=n%m
d=n//s
n=n%s
print(a,"xl ",b,"l ",c,"m ",d,"s ")'''

#5.
'''stk=[2,4,6,8]
def push(inte):
    if inte==10:
        stk.append(inte)
        print(stk)
push(10)
def pop():
    if stk==[]:
        print("Stack Empty")
    else:
        while stk!=[]:
            print(stk.pop())
        else:
            print("Underflow Error")
pop()
def peek():
    if stk==[]:
        print("Stack Empty")
    else:
            top=len(stk)-1
            print(stk[top],"<---TOP")
            for i in range(top-1,-1,-1):
                print(stk[i])
peek()'''
