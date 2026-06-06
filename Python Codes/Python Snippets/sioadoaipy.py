name=input("enter author name:")
titlebook=input("enter title of the book:")
priceofthebook=int(input("enter price of the book:"))
isbn=int(input("enter ISBN number of the book:"))
L=[]
L.append(name)
L.append(titlebook)
L.append(priceofthebook)
print(L)
def book(author,title,price):
    d={}
    d[isbn]=[author,title,price]
    return d

def price():
    for i in d:
        price1=d[i][2]
        if price1>30 and price1<500:
            price1-=30
        elif price1>500:
            price1-=0.1*price1
    
    print(price1)


d=book(name,titlebook,priceofthebook)
price()