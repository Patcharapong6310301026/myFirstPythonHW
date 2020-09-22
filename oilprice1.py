print("################################################################################")
print("##                            welcome to oil price                            ##")
print("##                                                                            ##")
print("##                                                                            ##")
print("##                                                                            ##")
print("##                                                                            ##")
#กำหนดค่าตัวแปร
gas95 = 29.16
gas91 = 25.30
gasohol91 = 21.68
e20 = 20.2
gasohol95 = 21.2
die = 21.1
print("##                             1  Gasoline95 29.16                            ##")
print("##                                                                            ##")
print("##                             2  Gasoline91 25.30                            ##")
print("##                                                                            ##")
print("##                             3  Gasohol91  21.68                            ##")
print("##                                                                            ##")
print("##                             4  GasoholE20 20.2                             ##")
print("##                                                                            ##")
print("##                             5  Gasohol95  21.1                             ##")
print("##                                                                            ##")
print("##                             6  Diesel     21.1                             ##")
print("##                                                                            ##")
print("##                                                                            ##")
print("################################################################################")
#กำหนดอัตราแลกเปลี่ยน
cal = int(input("\n1. money to litre\n2. litre to money\nSelect number :"))
if cal == 1 :
              print("\nMoney to litre")
              oil = int(input("Type of oil :"))
              while oil > 6 :
                    oil = int(input("Enter Type of oil Again:"))
              value = int(input("Money :"))
              if oil == 1 :
                  sums = value/gas95
                  print(sums,"liter")
              elif oil == 2 :
                  sums = value/gas91
                  print(sums,"liter")
              elif oil == 3 :
                  sums = value/gasohol91
                  print(sums,"liter")
              elif oil == 4 :
                  sums = value/e20
                  print(sums,"liter")
              elif oil == 5 :
                  sums = value/gasohol95
                  print(sums,"liter")
              elif oil == 6 :
                  sums = value/die
                  print(sums,"liter")
elif cal == 2:
              print("\nlitre to money")
              oil = int(input("Type of oil :"))
              while oil > 6 :
                    oil = int(input("Enter Type of oil Again:"))
              value = int(input("Liter  :"))
              if oil == 1 :
                  sums = value*gas95
                  print(sums,"bath")
              elif oil == 2 :
                  sums = value*gas91
                  print(sums,"bath")
              elif oil == 3 :
                  sums = value*gasohol91
                  print(sums,"bath")
              elif oil == 4 :
                  sums = value*e20
                  print(sums,"bath")
              elif oil == 5 :
                  sums = value*gasohol95
                  print(sums,"bath")
              elif oil == 6 :
                  sums = value*die
                  print(sums,"bath")
              else :
                   print("choice error'")
#ทำระบบลูปวน
else :
        print("Error")
        
ex = input("\nExit : ")
while True :
            if ex == "y":
                         print("EXIT")
                         break 
            else :
                      cal = int(input("\n1. money to litre\n2. litre to money\nSelect number :"))
                      if cal == 1 :
                                    print("\nMoney to litre")
                                    oil = int(input("Type of oil :"))
                                    while oil > 6 :
                                            oil = int(input("Enter Type of oil Again:"))
                                    value = int(input("Money :"))
                                    if oil == 1 :
                                        sums = value/gas95
                                        print(sums,"liter")
                                    elif oil == 2 :
                                        sums = value/gas91
                                        print(sum,"liter")
                                    elif oil == 3 :
                                        sums = value/gasohol91
                                        print(sums,"liter")
                                    elif oil == 4 :
                                        sums = value/e20
                                        print(sums,"liter")
                                    elif oil == 5 :
                                        sums = value/gasohol95
                                        print(sums,"liter")
                                    elif oil == 6 :
                                        sums = value/die
                                        print(sums,"liter")
                      elif cal == 2:
                                    print("\nlitre to money")
                                    oil = int(input("Type of oil :"))
                                    while oil > 6 :
                                            oil = int(input("Enter Type of oil Again:"))
                                    value = int(input("Liter  :"))
                                    if oil == 1 :
                                        sums = value*gas95
                                        print(sums,"bath")
                                    elif oil == 2 :
                                        sums = value*gas91
                                        print(sums,"bath")
                                    elif oil == 3 :
                                        sums = value*gasohol91
                                        print(sums,"bath")
                                    elif oil == 4 :
                                        sums = value*e20
                                        print(sums,"bath")
                                    elif oil == 5 :
                                        sums = value*gasohol95
                                        print(sums,"bath")
                                    elif oil == 6 :
                                        sums = value*die
                                        print(sums,"bath")
                                    else :
                                         print("choice error'")
                      else :
                              print("Error")
                              
                      ex = input("\nExit : ")
                      while True :
                                  if ex == "y":
                                               print("EXIT")
                                               break 
print("################################################################################")
print("##                                                                            ##")
print("##                                                                            ##")
print("##                                                                            ##")
print("##                           thank  you  for coming                           ##")
print("##                                                                            ##")
print("##                                                                            ##")
print("##                                                                            ##")
print("################################################################################")

 

