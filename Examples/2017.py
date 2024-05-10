import os
import math
from math import sin, cos
import re
import numpy as np


"""
y=1
x=3
name="Mo"
lst = [1,2,5,"bread"]
"""


"""
def greeting_generator(phrase):
	def greeting(name):
		print(phrase, name)
	return greeting
"""	


"""
def our_decorator(func):
	def function_wrapper(x):
		print("Before calling " + func.__name__)
		func(x)
		print("After calling " + func.__name__)
	return function_wrapper
	
def foo(x):
	print("Hi, foo has been called with " + str(x))
print("We call foo before decoration:")
foo("Hi")

print("We now decorate foo with f:")
foo = our_decorator(foo)
print("We call foo after decoration:")
foo(42)
"""


"""
def call_counter(func):
	def helper(x):
		helper.counter += 1
		return func (x)
	helper.counter = 0
	return helper

@call_counter	
def f(y):
	return y+22
	
sin = call_counter(sin)

print("f has been called " + str(f.counter) + " times!")
for i in range(10):
	print(f(i), sin(i))
	
print("f has been called " + str(f.counter) + " times!")
print("sin has been called " + str(sin.counter) + " times!")
"""


"""
from functools import wraps

def greeting(func):
	@wraps(func)
	def function_wrapper(x):
		#function_wrapper of greetings
		print("Hi, " + func.__name__ + "returns:")
		return func(x)
		
	return function_wrapper
"""


"""
def f(x):
	return x+1
	
g=lambda x : x+1

h=lambda x,y : x+y-5
"""

#comment

"""
class Robot:
	pass
	
	def __init__(self, name=None):
		self.name = name
		
	def robot_laws():
		print("A robot must obey its builder")

	def say_hi(self):
		if self.name:
			print("Hi I am " + self.name)
		else:
			print("Hi I am nameless")
		

x=Robot()
x.name = "Marvin"
x.energy = 0.8
x.charge = 100

y=Robot("Melvin")
z=Robot()

Robot.charge = "enough"
Robot.brand = "Kuka"

x.say_hi()
y.say_hi()
Robot.robot_laws()

print(x.charge)
"""


"""
a=np.array([0,1,2,3])
print(a)

celsius_values = [25.3, 24.8, 26.9, 23.9]
C=np.array(celsius_values)
print(C)
#turn into fahrenheit

print(C * 9/5+32)
"""



z=np.array ([1,2,3], np.int32)
print(z)
np.savetxt("test.txt", z)


x=np.array([2,3,2], np.int32)
y=np.array(["q","I","I2"])
print(x, y)
np.savetxt("test2.txt", x)


"""
a=np.genfromtxt("I_68.txt", skip_header=1, dtype=float, usecols=(0,1))
print(a[1])
a[:,1]*=2
np.savetxt("test.txt", a, delimiter="\t", newline="\r\n", fmt="%8.3f")
print(a[1])
"""

"""
import matplotlib.pyplot as plt

lst=[3,5,9,16,29]
x=[100,200,300,400,500]
plt.plot(x, lst)
plt.show()
"""


a=np.genfromtxt("I_68.txt", skip_header=1, dtype=float, usecols=(0,1))
print(a[2])
#a[:,1]*=2
np.savetxt ("test3.txt", a, delimiter="\t", newline="\r\n", fmt="%8.3f")
print(a[1])


