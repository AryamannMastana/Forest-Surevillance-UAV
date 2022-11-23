#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#Parameters used in the notebook
AR = 10;
e = 0.79;
S = 0.484;
b = 2.2;
chord_root = 0.294;
chord_tip = 0.147;
step_size = b/200;
g = 9.81;
W = S*155.59;
stress = 450 * 10**6;
thickness = 0.5*10**(-6);
pi = math.pi;


# In[4]:


#Chord Distribution of an equivalent(span and area same) Elliptic Distribution
c_ellipse = [];
span_array = [];
for i in range(102):
    y = (i-1)*step_size;
    span_array.append(y);
    c_ellipse.append(((4*S)/(pi*b))*math.sqrt(1-(2*y/b)**2));


# In[5]:


#Chord Distribution of our designed UAV
c_actual = [];
for i in range(102):
    c_actual.append((chord_root + ((chord_root - chord_tip)/(0-b/2))*span_array[i]));
    


# In[6]:


c_shrenk = []
for i in range(len(c_actual)):
    c_shrenk.append(0.5*(c_actual[i] + c_ellipse[i]))
    
c_shrenk = np.array(c_shrenk);
c_actual = np.array(c_actual);
c_ellipse = np.array(c_ellipse);


# In[7]:


#Run ONLY ONCE while running the script for the first time
c_shrenk = np.delete(c_shrenk,0);
c_actual = np.delete(c_actual,0);
c_ellipse = np.delete(c_ellipse,0);
span_array = np.delete(span_array,0);


# In[8]:


#Shrenk's Method Chord Distribution:
plt.plot(span_array,c_shrenk,label = 'Shrenk')
plt.plot(span_array,c_actual,label = 'Geometric')
plt.plot(span_array,c_ellipse,label = 'Ellipse')
plt.xlabel("Span")
plt.ylabel("Chord Distribution")
plt.legend()
plt.grid()
plt.xlim([0,1.2])
plt.ylim([0,0.3])
plt.title("Chord Distribution for Ellipse, Actual and Shrenk")
plt.show()


# In[9]:


#Actual Lift Coefficient
local_lift_coefficient = c_shrenk/c_actual;
plt.plot(span_array,local_lift_coefficient)
plt.xlabel("Span")
plt.ylabel("Local Lift Coefficient")
plt.grid()
plt.xlim([0,1.2])
plt.ylim([0,1.1])
plt.title("Local Lift Coefficient due to Shrenk's Approximation")
plt.show()


# In[10]:


#Actual Lift Distribution : Make sure that the lift due to wing (singular) equals the W/2
sum_lift = np.sum(local_lift_coefficient);
kappa = W/(2*sum_lift);
print("Kappa : ",kappa)
actual_lift = kappa*local_lift_coefficient;
plt.plot(span_array,actual_lift)
plt.xlabel("Span")
plt.ylabel("Lift Distribution due to Shrenk")
plt.grid()
plt.xlim([0,1.2])
plt.ylim([0,0.5])
plt.title("Lift Distribution due to Shrenk's Approximation")
plt.show()


# In[11]:


#Calculate the reactions at the support:
R_0 = np.sum(actual_lift);
M_0 = 0;
for i in range(101):
    M_0 = M_0 + actual_lift[i]*span_array[i];
print("R_0 : ", R_0)
print("M_0 : ", M_0)


# In[12]:


#Shear Force as a Function of span
shear_force = [];
for i in range(101):
    shear_lift = 0;
    for j in range(i):
        shear_lift = shear_lift + actual_lift[j];
    sum_shear = R_0 - shear_lift;
    shear_force.append(sum_shear);
shear_force = np.array(shear_force);
plt.plot(span_array,shear_force)
plt.xlabel("Span")
plt.ylabel("Shear Force Distribution")
plt.grid()
plt.xlim([0,1.2])
plt.ylim([0,40])
plt.title("Shear Force Distribution due to Shrenk's Approximation")
plt.show()


# In[18]:


#Bending Moment as a function of span:
bending_moment = [];
sum_moment = 0;
for i in range(101):
    moment_lift = 0;
    for j in range(i):
        moment_lift = moment_lift + actual_lift[j]*span_array[j]
    sum_moment = M_0 - shear_force[i]*span_array[i] - moment_lift;
    bending_moment.append(sum_moment);
plt.plot(span_array,bending_moment)
plt.xlabel("Span")
plt.ylabel("Bending Moment Distribution")
plt.grid()
plt.xlim([0,1.2])
plt.ylim([0,22])
plt.title("Bending Moment Distribution due to Shrenk's Approximation")
plt.show()


# In[29]:


#Moment of Inertia as a function of span:
moment_of_inertia = [];
for i in range(101):
    moment_of_inertia.append(bending_moment[i]*c_actual[i]/stress);
moment_of_inertia = np.array(moment_of_inertia);
plt.plot(span_array,moment_of_inertia)
plt.xlabel("Span")
plt.ylabel("Moment of Inertia Distribution")
plt.grid()
plt.xlim([0,1.2])
plt.ylim([0,1.4*10**-8])
plt.title("Moment of Inertia Distribution\n due to Shrenk's Approximation")
plt.show()


# In[28]:


#Spar-width as a function of span:
spar_width = moment_of_inertia*2/(thickness**2);
plt.plot(span_array,spar_width)
plt.xlabel("Span")
plt.ylabel("Spar Width Distribution")
plt.grid()
plt.xlim([0,1.2])
#plt.ylim([0,1.4*10**-8])
plt.title("Spar-Width Distribution due to Shrenk's Approximation")
plt.show()

