def romanToInt(s: str) -> int:


    rang_index = len(s)
    soma = int(0)
    num_index = 0

    for i in s:
        if i == "M":
            num_index += 1
            soma += 1000
            print("Laço M soma =", soma)
            print("Laço M reng_index =",rang_index)
            print("Index :",num_index)

        elif i == "D":
            num_index += 1
            if rang_index == num_index:
                soma += 500 
            elif s[num_index] == "M":
                soma -= 500
            else:
                soma += 500
            print("Laço C soma =", soma)
            print("Laço C reng_index =",rang_index)
            print("Index :",num_index)


        elif i == "C":
            num_index += 1
            if rang_index == num_index:
                soma += 100 
            elif s[num_index] == "D" or s[num_index] == "M":
                soma -= 100
            else:
                soma += 100
            print("Laço C soma =", soma)
            print("Laço C reng_index =",rang_index)
            print("Index :",num_index)

        elif i == "L":
            num_index += 1
            if rang_index == num_index:
                soma += 50 

            elif s[num_index] == "C" or s[num_index] == "D" or s[num_index] == "M":
                soma -= 50
            else:
                soma += 50
            print("Laço L soma =", soma)
            print("Laço L reng_index =",rang_index)
            print("Index :",num_index)

        elif i == "X":
            num_index += 1
            if rang_index == num_index:
                soma += 10 
            elif s[num_index] == "L" or s[num_index] == "C" or s[num_index] == "D" or s[num_index] == "M":
                soma -= 10
            else:
                soma += 10
            print("Laço X soma =", soma)
            print("Laço X reng_index =",rang_index)
            print("Index :",num_index)
        elif i == "V":
            num_index += 1
            if rang_index == num_index:
                soma += 5 
            elif s[num_index] == "L" or s[num_index] == "C" or s[num_index] == "D" or s[num_index] == "M":
                soma -= 5
            else:
                soma += 5
            print("Laço V soma =", soma)
            print("Laço V reng_index =",rang_index)
            print("Index :",num_index)
        elif i == "I":
            num_index += 1
            if rang_index == num_index:
                soma += 1 
            elif s[num_index] == "V" or s[num_index] == "X" or s[num_index] == "L" or s[num_index] == "C" or s[num_index] == "D" or s[num_index] == "M":
                soma -= 1
                print("laço I if ",i)
                print(soma)
            else:        
                soma += 1

            print("Laço I soma =", soma)
            print("Laço I reng_index =",rang_index)
            print("Index :",num_index)

    print(soma)
    return soma

num_Romano = input("Enter a roman number: ")
romanToInt(num_Romano)