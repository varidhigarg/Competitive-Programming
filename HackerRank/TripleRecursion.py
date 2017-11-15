'''
You are filling a matrix by following a set of rules. Given a square matrix of size , where  is its upper-left cell and  is its bottom-right cell, fill all the cells according to the following rules:

Value of  is defined recursively as follows:

if  and  then 
else if  then 
else if  then 
else, if , then 
In other words, given integers  and , the matrix is filled by putting  in the upper-left cell, and then every other cell  on the main diagonal of the matrix is filled with the value . Remaining cells of the matrix are filled according to the two other recursive rules defined above.

For example, for , , , the matrix will be:-

3 2 1 0
2 4 3 2
1 3 5 4
0 2 4 6
The task is to print the matrix after all its cells are filled with values.

Input Format

In the first and only line of the input, there are  space-separated integers , , and , where  is the size of the matrix and both  and  denote values used in the recursive definition in the statement.

Constraints

Output Format

Output the matrix with exactly  lines. In the  line, print  space-separated integers denoting the  row of the matrix with all cells filled with appropriate values.

Sample Input 0

5 10 7
Sample Output 0

10 9 8 7 6
9 17 16 15 14
8 16 24 23 22
7 15 23 31 30
6 14 22 30 38
'''


#!/bin/python

import sys

def tripleRecursion(n, m, k):
    res = []
    for x in range(2):
        res.append([])
        for y in range(n):
            res[x].append(0)
    res[0][0]=m
    for x in range(n):
        for y in range(n):
            if x==y:
                if x>0:
                    res[x%2][x] = res[x%2-1][x-1] + k
            elif x>y:
                res[x%2][y] = res[x%2-1][y] - 1
            else:
                res[x%2][y] = res[x%2][y-1] - 1
            print res[x%2][y],
        print ""
                
    

if __name__ == "__main__":
    n, m, k = raw_input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    tripleRecursion(n, m, k)
