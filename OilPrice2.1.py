import os
import time

from zeep import Client
from lxml import etree

client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')

def respond():
    while True:
        w = int(input("Are you want to end? press 1 if Yes"))
        if w == 1 :
            return True

check = True
while check:
      # Comment
      print("Oil Sale System")
      print("Codecreater:Patcharapong")
      print("Create at 20/09/2020")
      # Get Data from website
      result = client.service.CurrentOilPrice(Language="en")
      root = etree.fromstring(result)
      d = len(root)
      name = ['none']
      price = [0]
      for i in range(d):
          if len(root[i]) == 3:
              name.append(root[i][1].text)
              price.append(float(root[i][2].text))
      print("### Cost ###")
      for i in range(1, len(name)):
          print("{}. {} : {} BAHt".format(i, name[i], price[i]))
      print("###Oil Service###")
      pas = input("Are you want Service now?(1 yes or 0 if no): ")     
      if pas == "9999":
          check = False
          break
      start = int(pas)
      if start ==1:
          letgo = True
      else:
          letgo = False
      while letgo:
          n = 2
          k = 0
          print("Get Liters by Money(0) \n Get Money by Liters(1)")
          while n > 1:
              n = int(input("Press a number(0,1): "))
          while k == 0:
              k = int(input("Choose kind of cal (1-{len(name)-1}): "))
          if n == 0:
              m = float(input("Enter the money: "))
              res = m / price[k]
              print("The liters: {res} 1")
              letgo = False
          else:
              m = float(input("Enter the liters:"))
              res = m * price[k]
              print("Total :{res} Baht")
              letgo =False
      if respond():
          print("Thank you for coming")
          time.sleep(3)
          os.system('cls')  
                

      
