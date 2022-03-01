from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def func(x):
    return x

interact(func, x="Hello")

def g(x, y):
    return (x,y)