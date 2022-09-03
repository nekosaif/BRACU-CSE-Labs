# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 08:14:45 2021

@author: Mollah Md. Saif
"""


import abc


#Stack interface
class Stack(abc.ABC):
    @abc.abstractmethod
    def push(self):
        pass
    
    @abc.abstractmethod
    def pop(self):
        pass
    
    @abc.abstractmethod
    def peek(self):
        pass


#ArrayStack class implementing Stack interface
class ArrayStack(Stack):
    def __init__(self):
        self.stack = []
        self.pointer = -1
    
    def push(self, data):
        self.stack.append(data)
        self.pointer += 1
            
    def pop(self):
        if self.pointer == -1:
            raise RuntimeError("StackUnderflow")
        val = self.stack[self.pointer]
        self.stack = self.stack[:-1]
        self.pointer -= 1
        return val
    
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[self.pointer]


#LinkedListStack class implementing Stack interface  
class LinkedListStack(Stack):
    class __Node:
        def __init__(self, data, next_node):
            self.data = data
            self.next_node = next_node
        
    def __init__(self):
        self.head = None
        
    def push(self, data):
        if self.head == None:
            self.head = self.__Node(data, None)
            return
        self.head = self.__Node(data, self.head)
            
    def pop(self):
        if self.head == None:
            raise RuntimeError("StackUnderflow")
        ret_node_data = self.head.data
        del_node = self.head
        self.head = self.head.next_node
        del del_node
        return ret_node_data
        
    def peek(self):
        if self.head == None:
            return None
        return self.head.data


def parenthesis_balancing(s, stack_type = ArrayStack):
    correct_msg = 'This expression is correct.'
    incorrect_msg = 'This expression is NOT correct.'
    error_msg = lambda i, c, s: f'Error at character # {i}. ‘{c}‘- not {s}.'
    stack_parenthesis = stack_type()
    stack_index = stack_type()
    i = 0
    for c in s:
        i += 1
        if c in '(){}[]':
            if c in '({[':
                stack_parenthesis.push(c)
                stack_index.push(str(i))
            else:
                if stack_parenthesis.peek() != None:
                    top = stack_parenthesis.peek()
                    top = '' if top == None else top
                    if top+c in ['()', '{}', '[]']:
                        stack_parenthesis.pop()
                        stack_index.pop()
                    else:
                        print(incorrect_msg)
                        print(error_msg(stack_index.peek(), stack_parenthesis.peek(), 'closed'))
                        return
                else:
                    print(incorrect_msg)
                    print(error_msg(i, c, 'opened'))
                    return
    if stack_parenthesis.peek() != None:
        print(incorrect_msg)
        print(error_msg(stack_index.peek(), stack_parenthesis.peek(), 'closed'))
        return
    print(correct_msg)
                

def tester():
    inp_str = ['1+2*(3/4)',
               '1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14',
               '1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14',
               '1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14']
    
    print('________________ArrayStack________________')
    for i in inp_str:
        print(i)
        parenthesis_balancing(i, ArrayStack)
        if i != inp_str[-1]:
            print()
    print('__________________________________________\n\n')
    
    print('______________LinkedListStack_____________')
    for i in inp_str:
        print(i)
        parenthesis_balancing(i, LinkedListStack)
        if i != inp_str[-1]:
            print()
    print('__________________________________________\n')


def main():
    tester()
    
    
if __name__=='__main__':
    main()