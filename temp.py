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

x=5
print(x)

def add_numbers(w, e, r):
    a = w + e
    b = w + r
    c = r + sin(r)
    print(a, b, c,)

add_numbers(1, 2, 3) #runs the function while transmiting the values 1,2,3 for w,e,r

print(math.sqrt(4))
print(np.pi)
print("\n")
print("Hello World!")

path = os.getcwd()
print("we are in ")
print(path)

print(dir)
print(os.getcwd())
print(os.listdir())

print("we are in " + os.getcwd())

original = r'New.py'
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

"""
name = input("Enter your name: ")
print("Hello", name)
"""

"""
def test(x):
	y=x*2
	return y


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
"""






