import os
from os import listdir, system
import math
import re
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
from math import sin, cos
from os import listdir, system
import shutil

def add_numbers(w, e, r):
    a = w + e
    b = w + r
    c = r + sin(r)
    print(a, b, c,)

add_numbers(1, 2, 3)

print("\n")
print(math.sqrt(4))
print(np.pi)
print("\n")
print("Hello")

path = os.getcwd()

print("we are in ")
print(dir)
print(path)


x=5
print ('Mo')
print (x)
print (dir)
print (os.getcwd())
print (os.listdir())

original = r'Ohne Titel.py'
target = r'Programs'
#shutil.move(original,target)

#mkdir("New")

"""
print (os.getcwd())
path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
print (os.getcwd())

#os.chdir("..")
"""

name = input("Enter your name: ")
print("Hello", name)



import math
import os
import numpy as np

def test(x):
	y=x*2
	return y

print ("we are in " + os.getcwd())
path = os.getcwd()

print ("\n")

print ("we are in ") 
print (path)

shopping_list=['a', 'b']

def foo(x):
    return x + 12

def bar(y):
    return y*5

def foobar(x,y):
    return foo(x) + bar(y+1)


class Robot:
	
	def __init__(self, name = "Mel" , city = "Hamburg"):
		self.set_name(name)
		self.set_city = city
	
	def get_name(self):
		return self.__name

	def set_name(self, name):
		if name == "Henry":
			self.__name = "Mel"
		else:
			self.__name = name

	def say_hi(obj):
		print("Hi I am " + obj.get_name())


