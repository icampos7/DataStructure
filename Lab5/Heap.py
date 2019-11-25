# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:05:23 2019

@author: Isaac
Class: CS 2302
Instructure: Diego Aguirre
Assigment: Lab 5 LRU
TA Gerardo Barraza
"""
import math
class Heap:
    def __init__(self,word):
        self.heap = []
        #self.wordSet = set()
        self.wordH = word
        self.count = 1#count words
    def isEmpty(self):
        return len(self.heap) == 0
    def parent(self,index):
        if index == 0:
            return -math.inf
        pList = self.heap[(index - 1) // 2]
        return pList[1]
    #return the right index
    def rightChild(self,index):
        indexR = 2 * index + 2
        if indexR >= len(self.tree):
            return -math.inf
        rList = self.heap[indexR]
        return rList
    #return the left index 
    def leftChild(self,index):
        indexL = 2 * index + 1
        if index >= len(self.tree):
            return -math.inf
        indexL = self.heap[index]
        return indexL[1]
    #insert data in heap
    def insert(self,data):
        self.heap.append(data)
        self.percolateUp(len(self.heap) - 1)
        #balance heap
    def percolateUp(self,index):
        if index == 0:
            return
        indexP = (index - 1) // 2
        Valparent = self.heap[indexP]
        indexChild = self.heap[index]
        if indexP.count < indexChild.count:
            self.heap[index],self.heap[Valparent] = self.heap[indexP],self.heap[index]
            self.percolateUp(indexP)
        elif Valparent.count == indexChild.count and Valparent.wordH < indexChild.wordH:
            self.heap[index],self.heap[Valparent] = self.heap,self.heap[index]
            self.percolateUp(indexP)
def printMethod(word):
    h = Heap(word)
    for i in word:
        h.insert(word)
    for j in range(len(h.heap)):
        print(str(h.heap[i].word))
def main():
    FileWords = []
    with open("Test.txt") as file:
        line = file.readline().split()
        while line:
            FileWords.extend(line)
            line = file.readline().split()
        printMethod(line)
        
main()            