a="Hello,"
b="World!"
print(a+b)

x=int(input("Zahl 1:"))
while x==0:
    print("Ungültige Eingabe")
    x=int(input("Gib Zahl 1 nochmal ein:"))
    
y=int(input("Zahl 2:"))
while y==0:
    print("Ungültige Eingabe")
    y=int(input("Gib Zahl 1 nochmal ein:"))
print("Ergebnis der Adittion:",x+y)
print("Ergebnis der Subtraktion:",x-y)
print("Ergebnis der Multiplikation:",x*y)
print("Ergebnis der Division:",x/y)


    