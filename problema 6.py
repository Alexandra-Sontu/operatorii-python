n=2567
x=n%10 #unitatile numarului n
print(x,"ultima cifra a numarului n")
y=(n%100)//10 #zecimile numarului n"
print(y,"penultima cifra a numarului n")
print(n,"//",9,"=",n//9)
print(n,"%",9,"=",n%9)
print(2,"+",5,"+",6,"+",7,"=",2+5+6+7)
z=(n%1000)//100 #sutimile numarului n
g=n//1000 #miimile numarului n
p=1000*x+100*y+10*z+g
print(p,"rasturnatul numarului")
