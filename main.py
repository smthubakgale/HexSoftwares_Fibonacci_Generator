"""
Author : Thubakgale Mabalane (Sam)
Description: A simple program to generate a fibonacci sequence by taking user input about the length
"""

import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def fibo(num):
  if num <= 1:
      return 1
  return fibo(num - 1) + fibo(num - 2)

def fibonacci(num):
  arr = []
  for i in range(num):
      arr.append(fibo(i))
  return arr

if __name__ == "__main__":
    print("Hex software Fibonacci Sequence Generator")
    print("Welcome , press Enter to Continue")

    input()
    clear_screen()

    cn = True
    while cn:
        print("Enter length of sequence : ")
        str = input()
        
        try:
            num = int(str)

            seq = fibonacci(num)
            print(seq)

            input()
            clear_screen()
        except:
            print("incorrect input")
