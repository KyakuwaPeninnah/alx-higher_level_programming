#!/usr/bin/python3
'''task 9 module'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square'''
    def __init__(self, size):
        '''initialization of square'''
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        '''gets that number'''
        return self.__size ** 2
