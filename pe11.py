#!/usr/bin/python
size=2
matrix=[[0 for i in range(size)] for j in range(size)]

for i in range(size):
    for j in range(size):
        matrix[i][j]=raw_input()
print matrix        
