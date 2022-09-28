"""
You are given two lists linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

l1 = [2,4,3]
l2 = [5,6,4]

def addTwoNumbers(l1, l2):
    multip = 0
    resultado_l1 = 0
    resultado_l2 = 0

    for x in l1:
        if multip == 0:
            resultado_l1 = x
            multip = 1
            print(resultado_l1)
            print(x)
        elif multip != 0:
            print('------------------')
            print(x)
            resultado_l1 += multip*(10)*x
            multip = multip * 10
            print(resultado_l1)

    multip = 0

    for x in l2:
        if multip == 0:
            resultado_l2 = x
            multip = 1
            print(resultado_l2)
            print(x)
        elif multip != 0:
            resultado_l2 += multip*(10)*x
            multip = multip * 10

    resultado_l1 += resultado_l2
    return resultado_l1

addTwoNumbers(l1,l2)





