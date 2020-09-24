print("######################################################")
print("##                                                  ##")
print("##                                                  ##")
print("##                                                  ##")
print("##             welcome to a coffee shop             ##")
print("##                                                  ##")
water = int(400) 
milk  = int(540)
beans = int(120)
dis =int(9)
money = int(550)
print("######################################################")
print("##                                                  ##")
print("##                                                  ##")
print("##             what action do you want              ##")
print("##                                                  ##")
print("##                                                  ##")
print("##                                                  ##")
print("##                                                  ##")
print("##                                                  ##")
print("##                                                  ##")
print("######################################################")
act =int(input("\n1. buy\n2. fill\n3. take\nSelect number :"))
#buy
if act == 1 :
             print("\nWhat coffee are you want")
             cof = int(input("\n1.espresso\n2.latte \n3.cappuccino\n:"))
             while  cof > 3 :
                    cof = int(input("please try again:"))
             if cof == 1 :
                water -= 250
                beans -= 16
                money += 4
                dis   -= 1
             elif cof == 2 :
                 water -= 150
                 milk  -= 75
                 money += 7
                 dis   -= 1 
             elif cof == 3 :
                 water -= 50
                 milk  -= 100
                 beans -= 20
                 money += 6
                 dis   -= 1
             print(water,milk,beans,dis,money)
#fill
if act == 2 :
             print("*****What kind are you fill?*****")
             fit = int(input("\n1.water\n2.milk\n3.coffee bean\n4.disposable cup\n:"))
             while fit > 4 :
                   fit = int(input("Pls try again:"))
             if fit == 1 :
                wet = int(input("How many ml of water do you want to add?:\n"))
                water += wet 
             print(water)
             if fit == 2 :
                wet = int(input("How many ml of milk do you want to add?:\n"))
                milk += wet 
             print(milk)
             if fit == 3 :
                wet = int(input("How many grams of coffee beans do you want to add?:\n"))
                beans += wet 
             print(beans)
             if fit == 4 :
                wet = int(input("How many disposable cups of coffee do you want to add?:\n"))
                dis += wet 
             print(dis)
if act == 3 :
            print("I gave you",money)
   
   
   
   

