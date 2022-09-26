"""
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

"""

numero_inteiro = input('Digite um numero inteiro para tranformar em Romano: ')
len_numero = len(numero_inteiro)
cont_len = len_numero
romanos = numero_inteiro
romanos = int(romanos)


print(type(romanos))

def Romanos(numero_inteiro, cont_len,romanos):
    # Casa dos milhares
    m = ["","M","MM","MMM"]
    #Casa das centenas
    c = ["", "C", "CC", "CCC", "CD" ,"D" ,"DC" ,"DCC" ,"DCCC" ,"CM"]
    #Casa das dezenas
    x = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    #Casa das unidades
    i = ["","I","II","III","IV","V","VI","VII","VIII","IX"]

    unidades = ""
    dezenas = ""
    centenas = ""
    milhares = ""
    
    for z in numero_inteiro:
        print("ContLen laço for",cont_len)
        if cont_len == 4:
            print(type(romanos))
            milhares = m[romanos // 1000]
            cont_len -= 1
            print("ContLen ",cont_len)

        if cont_len == 3:
            centenas = c[(romanos % 1000) // 100]
            cont_len -= 1
            print("ContLen ",cont_len)            
        
        if cont_len == 2:
            print(type(romanos))
            dezenas = x[(romanos % 100) // 10]
            cont_len -= 1
            print("ContLen ",cont_len)

        if cont_len == 1:
            print(type(romanos))
            unidades = i[romanos % 10]
            print("ContLen ",cont_len)

        romtoint = (milhares + centenas + dezenas + unidades)
    print(romtoint)
    return romtoint

Romanos(numero_inteiro,cont_len,romanos)

