# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:57:07 2019

@author: APL14
"""

inputMatrix = [[0,5,0,3,0,0,0,7,0],
               [2,0,0,7,0,0,5,0,4],
               [0,0,3,0,0,0,0,0,8],
               [0,0,1,2,3,0,0,0,9],
               [0,0,0,4,0,7,0,0,0],
               [8,0,0,0,9,1,2,0,0],
               [7,0,0,0,0,0,3,0,0],
               [3,0,4,0,0,2,0,0,7],
               [0,1,0,0,0,3,0,8,0]]

# inputMatrix = [[0,0,0,0,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0],
#                [0,0,0,0,0,0,0,0,0]]

nums = [1,2,3,4,5,6,7,8,9]

def checkIfValidRow(num, row, col):
    if(num==0):
        return True
    rowArr = inputMatrix[row]
    for el in rowArr:
        if(num==el):
            return False
    return True

def checkIfValidColumn(num, row, col):
    if(num==0):
        return True
    colArr = []
    for arrs in inputMatrix:
        colArr.append(arrs[col])
    for el in colArr:
        if(num==el):
            return False
    return True

def checkIfValidSector(num, row, col):
    if(num==0):
        return True
    sectorArr = []
    if(row>=0 and row <=2):
        rowindices = [0,1,2]
    if(row>=3 and row <=5):
        rowindices = [3,4,5]
    if(row>=6 and row <=8):
        rowindices = [6,7,8]
    if(col>=0 and col <=2):
        colindices = [0,1,2]
    if(col>=3 and col <=5):
        colindices = [3,4,5]
    if(col>=6 and col <=8):
        colindices = [6,7,8]
    
    for i in rowindices:
        for j in colindices:
            sectorArr.append(inputMatrix[i][j])
    for el in sectorArr:
        if(num==el):
            return False
    return True

def checkAllValid(num, row, col):
    isValid = checkIfValidRow(num, row, col) and checkIfValidColumn(num, row, col) and checkIfValidSector(num, row, col)
    return isValid

def readOnlyIndices():
    arr = []
    for i in range (0,9):
        for j in range(0,9):
            if(inputMatrix[i][j]!=0):
                arr.append([i,j])
    return arr

def recursiveFill2(row, col):
    # print(str(row)+","+str(col))
    ret = False
    if [row,col] in arr:
        if(col==8 and row==8):
            return True
        elif(col==8):
            ret = recursiveFill2(row+1, 0)
        else:
            ret = recursiveFill2(row, col+1)
        if(ret):
            return True
    else:
        for i in range(1,10):
            if(checkAllValid(i, row, col)):
                inputMatrix[row][col] = i
                if(col==8 and row==8):
                    return True
                elif(col==8):
                    ret = recursiveFill2(row+1, 0)
                else:
                    ret = recursiveFill2(row, col+1)
                if(ret):
                    return True
        inputMatrix[row][col] = 0
    return False


arr = readOnlyIndices()

recursiveFill2(0,0)