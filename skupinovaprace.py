opakovat = "ano"
while opakovat == "ano":
    čísloJedna = int(input("Zadejte číslo:"))
    čísloDva = int(input("Zadejte druhé číslo:"))
    znamínko = int(input("Zadejte znamínko:"))
    if znamínko == "+":
        print(čísloJedna + čísloDva)
    elif znamínko == "-":
        print(čísloJedna - čísloDva) 
    elif znamínko == "*":
        print(čísloJedna * čísloDva) 
    elif znamínko == "/":
        print(čísloJedna / čísloDva)
    else:
        print("neplatné znamínko")
    opakovat = input("chcete zopakovat:")            