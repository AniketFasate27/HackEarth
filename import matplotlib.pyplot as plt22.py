import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.axis import Axis
import csv

x=[]
y=[]

a=[]
b=[]

with open('a.csv', 'r') as csvfile:
    plots= csv.reader(csvfile)
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
    c = max(x)
    

with open('a.csv', 'r') as csvfile:
    plots1= csv.reader(csvfile)
    for row in plots1:
        a.append(int(row[0]))
        b.append(int(row[2]))


plt.figure(1)
plt.plot(x,y,marker='o', color='k')

plt.grid() 

plt.title(c)

plt.xlabel('Number of People')
plt.ylabel('Expenses')

plt.figure(2)
plt.plot(a,b, marker='o',color='k')
plt.xlabel('Number ')
plt.ylabel('Expenses')
plt.grid() 
plt.show()