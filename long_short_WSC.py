print("Welcome")
n=int(input("Please enter the number of trades: "))
l=0
s=0
while n>0:
    y=input('Type of trade: ')
    y=y.lower()
    if y == 'long':
        l+=1
        n-=1
    elif y == 'short':
        s+=1
        n-=1
    else:
        print('Please enter long or short only')
print("Here is the total data: ")        
print('Long=',l)
print('Short=',s)
print("Thanks!")