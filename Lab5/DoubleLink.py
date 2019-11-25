# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:14:30 2019

@author: Isaac
"""
class DoubleLink:
    def __init__(self,data,key):
        self.next = None
        self.prev = None
        self.head = None
        self.tail = None
        self.data = data#key
        self.key = key
    def insertBeforeHead(self,newData):
        newNode = DoubleLink(data = newData)
        newNode.next = self.head
        newNode.prev = None
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
    def insertAfter(self,prevNode,newData):#insert node after head Example "head 1 -> 2 -> 3 newNode
        if prevNode is None:
            return 
        newNode = DoubleLink(self,data = newData)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        
        if newNode.next is not None:
            newNode.next.prev = newNode
    def Append(self,newData):#append ---> Tail
        newNode = DoubleLink(data = newData)
        tail = self.head
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        while self.tail.next is not None:
            self.tail = tail.next
        self.last.next = newNode
        newNode.prev = tail
        # class LRU:
