'''
Problem: Triangle Quest 2.
Description: Given an integer n.
Print a palindromic triangle of size n.
Points: 20.

'''


for i in range(1, int(input())+1):
    print (((10**i - 1)//9)**2)