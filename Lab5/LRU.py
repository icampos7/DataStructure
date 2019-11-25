# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:45:22 2019

@author: Isaac Campos
"""
from DoubleLink import DoubleLink
class LRU:
    def __init__(self,cap = 4):
        self.size = cap
        self.count = 0
        self.dictionary = {}
    def get(self,key):
        if self.data in self.dictionary:
            node = self.dictionary[self.key]
            if node is self.tail or len(self.dictionary) == 1:
                return node.self.val
            elif node is self.head:
                return self.insertBeforeHead(self.head,self.data)
            else:
                return self.insertAfter()
    def put(self,key,value):
      newNode = DoubleLink(key,value)
      if self.head is None:
          self.insertAfter(value)
          self.count = self.count + 1
      elif self.count < self.size:#if the count is less then the max keep inserting 
          self.Append(value)
          self.count = self.count + 1
      else:
          self.count(value)
      self.dictionary[self.key] = newNode
    def size(self):
        return self.count
    def max_capacity(self):
        return self.size
    def print_Cache(self):
        temp = self.head
        while temp is not None:
            if temp.next is None:
                print(str(temp.key), "<--")
        print(str(temp.key) + "<->",end = '')
        temp = temp.next
    def print_Dictionary(self):
        for self.key in self.dictionary.key():
            print(str(key) + str(self.dictionary[key].data))
      #return
def main():
    LeastRU = LRU(3)
    LeastRU.put("Z",0)
    LeastRU.put("A",1)
    LeastRU.put("B",2)
    LeastRU.print_Dictionary()
    LeastRU.print_Cache()
    print()