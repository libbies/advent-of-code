#!/usr/bin/env python3
m = open('list.txt','r').readlines()

print(sum([(int(n)//3)-2 for n in m if n]))
