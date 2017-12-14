# Anika Kashyap
# 12/11/17
# Fuction Pracctice

import math

def cheese ():
    '''Makes a screen full of I like cheeses!!!'''
    print ( "I like cheese!" * 1000)

def temp_C (temp_F):
    ''' Converts a temperture in Fahrenheit to Celsius'''
    answer = (temp_F - 32) * 5/9
    return answer

def volume_sphere (radius):
    ''' Calculate the volume of a sphere'''
    volume = (4/3) *math.pi*r**3
    print ("Calculating")
    return volume

def I_love_puppies_and_dogs ():
    '''Make a screen full of I love puppies and dogs'''
    print (" I love puppies and dogs soooooooooooooo much" * 1543)

#cheese ()

I_love_puppies_and_dogs()

t_in_F = input (" Please enter a temperature in Farenhiet: ")
t_in_F = float(t_in_F)
t_in_C = temp_C(t_in_F)
print (" That temperture in Celsiusis",t_in_C)

r = input ("Please enter a radius of a sphere: ")
r = float (r)
print (" The volume of the sphere is", volume_sphere)
