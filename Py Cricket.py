print('---------------------------------------------------------')
print('|  _ _            _ _   _ _  _ _ _   _ _        _ _ _ _ |')                          
print('| |   - \  /     |     |   |   |    |     |  / |     |  |')
print('| |- -   \/      |     |- -    |    |     |--  |- -  |  |')
print('| |      /       |_ _  |  \  __|__  |_ _  |  \ |_ _  |  |')
print('|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|')


import random
def cric():
    l1 = ['HEADS','TAILS']
    l2 = ['BATTING','BOWLING']
    toss = random.choice(l1)
    ht = input("'Heads' or 'Tails' : ")
    if ht.upper() == toss:
        tex = 'It is ' + toss
        print('You won the toss')
        ubb = input("Choose batting or bowling : ")
        if ubb == 'batting' or ubb == 'bat':
            s1 = 0
            s2 = 0
            while(True):
                n1 = int(input("Enter the number to bat(from 0 to 10) : "))              #PLAYER CHOSE FOR BATTING
                cri = random.randint(0,10)
                if n1 == cri:
                    print('OUT')
                    print("SCORE OF PLAYER IS :",s1)
                    print("TARGET IS :",s1+1)
                    print("NOW YOU ARE BOWLING")                                
                    break
                else:
                    s1 += n1                                                              #COMPUTER IS BOWLING
                    print("COMPUTER KEPT :",cri)
                    print("PLAYER TOTAL :",s1)
            while(True):
                n2 = int(input("Enter the number to bowl from(0 to 10) : "))
                cri = random.randint(0,10)
                if cri == n2:
                    print('OUT')
                    print("SCORE OF COMPUTER IS :",s2)                                      #PLAYER IS BOWLING  
                    print("PLAYER WON THE MATCH")
                    break
                else:
                    s2 += cri
                    print("COMPUTER KEPT :", cri)                                              #COMPUTER IS BATTING
                    print("COMPUTER TOTAL :", s2)
                    if s2 > s1:
                        print("COMPUTER WON THE MATCH")
                        print("SCORE OF COMPUTER IS :",s2)
                        break
        elif ubb == 'bowling' or ubb == 'bowl':
            tc = 0
            tu = 0
            while(True):
                x1 = int(input("Enter the number to bowl from(0 to 10) : "))                  #PLAYER CHOSE FOR BOWLING
                cri = random.randint(0,10)
                if x1 != cri:
                    print('OUT')
                    print("SCORE OF COMPUTER IS :",tc)
                    print("TARGET IS :",tc+1)
                    print("NOW YOU ARE BATTING")
                    break
                else:                                                                               #COMPUTER IS BATTING
                    tc += cri
                    print("COMPUTER KEPT :",cri)
                    print("COMPUTER TOTAL :",tc)
            while(True):
                x2 = int(input("Enter the number to bat(from 0 to 10) : "))                      #PLAYER IS BATTING NOW
                cri = random.randint(0,10)
                if x2 == cri:
                    print('OUT')
                    print("SCORE OF PLAYER IS :",tu)
                    print("COMPUTER WON THE MATCH")
                    break
                else:
                    tu += x2
                    print("COMPUTER KEPT :",cri)                                                  #COMPUTER IS BOWLING
                    print("PLAYER TOTAL :",tu)
                    if tu > tc :
                        print("PLAYER WON THE MATCH")
                        print("SCORE OF PLAYER IS :",tu)
                        break       
                            
                    
    else:
        bb = random.choice(l2)
        print('It is',toss)
        print('You loss the toss')
        print('Computer chose',bb)
     
        if bb == 'BATTING':
            s1 = 0
            s2 = 0
            while(True):
                n1 = int(input("Enter the number to bowl(from 0 to 10) : "))           #COMPUTER CHOSE FOR BATTING
                c1 = random.randint(0,10)
                if n1 == c1:
                    print('OUT')
                    print("SCORE OF COMPUTER IS :",s1)
                    print("TARGET IS :",s1+1)
                    print("NOW YOU ARE BATTING")
                    break
                else:
                    s1 += c1
                    print("COMPUTER KEPT :",c1)
                    print("COMPUTER TOTAL :",s1)
            while(True):                                                             #COMPUTER IS BOWLING NOW
                n2 = int(input("Enter the number to bat from(0 to 10) : "))
                c2 = random.randint(0,10)
                if c2 == n2:
                    print('OUT')
                    print("SCORE OF PLAYER IS :",s2)
                    print("COMPUTER WON THE MATCH")
                    break
                else:
                    s2 += n2
                    print("COMPUTER KEPT :",c2)
                    print("PLAYER TOTAL :",s2)
                    if s2 > s1:
                        print("PLAYER WON THE MATCH")
                        print("SCORE OF PLAYER IS :",s2)
                        break
                    
        elif bb == 'BOWLING':
            tu = 0
            tc = 0
            while(True):
                x1 = int(input("Enter the number to bat from(0 to 10) : "))                          #COMPUTER CHOSE FOR BOWLING
                c1 = random.randint(0,10)
                if x1 == c1:
                    print('OUT')
                    print("SCORE OF PLAYER IS :",tc)
                    print("TARGET IS :",tc+1)
                    print("NOW YOU ARE BOWLING")
                    break
                else:
                    tc += x1
                    print("COMPUTER KEPT :",c1)
                    print("PLAYER TOTAL :",tc)
                
            while(True):
                x2 = int(input("Enter the number to bowl(from 0 to 10) : "))                         #COMPUTER IS BATTING NOW
                c2 = random.randint(0,10)
                if x2 == c2:
                    print('OUT')
                    print("SCORE OF COMPUTER IS :",tu)
                    print("PLAYER WON THE MATCH")
                    break
                else:
                    tu += c2
                    print("COMPUTER KEPT :",c2)
                    print("COMPUTER TOTAL :",tu)
                    if tu > tc :
                        print("PLAYER WON THE MATCH")
                        print("SCORE OF PLAYER IS :",tu)
                        break
cric()     