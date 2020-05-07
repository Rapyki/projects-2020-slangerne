# Importing useful packages 
import numpy as np
import scipy as sp
import sympy as sm
import matplotlib.pyplot as plt
import ipywidgets as widgets
import pylab
from scipy.misc import derivative

from numpy import array
from scipy import linalg
from scipy import optimize

sm.init_printing(use_unicode=True)

from sympy import *

# The linear demand function:
def p_total(qo,qi,a,b):
    """ solve for the inverse linear demand function

        Args:
            qo (symbol): produced qauntity by firm 0
            qi (symbol): produced qauntity by firm i
            a (symbol): demand parameter
            b (symbol): demand elasticity

        Returns:
            result (symbol): the solution represented as a symbol

    """ 

    return (a-b*(qo+qi))

def cost_f(qi,k):
    """ solve for the total cost of production of firm i

        Args:
            qi (symbol): produced qauntity by firm i
            k (symbol): marginal cost of production

        Returns:
            result (symbol): the solution represented as a symbol

    """ 

    return k*qi

#The profitfunction of firm i:
def profit_i(qo,qi,a,b,k):
    """ solve for the profit of firm i

        Args:
            qo (symbol): produced qauntity by firm 0
            qi (symbol): produced qauntity by firm i
            a (symbol): demand parameter
            b (symbol): demand elasticity
            k (symbol): marginal cost of production

        Returns:
            result (symbol): the solution represented as a symbol

    """ 

    return (p_total(qo,qi,a,b) * qi - cost_f(qi,k))


def solution_cournot(N,a,b,k):
    """ solve for optimal solution of the cournot model

        Args:
            N (symbol): The number of firms in the model
            a (symbol): demand parameter
            b (symbol): demand elasticity
            k (symbol): marginal cost of production

        Returns:
            result (RootResults): the solution represented as a RootResults object

    """ 
    
    # Note: This solution works for N firms with same cost function. 

    qo = sm.symbols('q_o')
    q = sm.symbols('q')
    qi = sm.symbols('q_i') #quantity of the N firm 

    foc_i = diff(profit_i(qo,qi,a,b,k),qi)

    # All firms have the same FOC so we will sum this up to get the total quantity and price

    foc_total = foc_i.replace(qo,q-qi) # Replaces using the definition qo = q - qi
    foc_total = foc_total*N # Multiplying the FOC for number of firms 
    foc_total = foc_total.replace(qi,q/N) # Replace qi * N with q

    total_quantity = simplify(sm.solve(sm.Eq(foc_total,0),q)[0])
    price = p_total(total_quantity-qi,qi,a,b)

    i_quantity = total_quantity/N

    i_profit = simplify(profit_i(total_quantity-i_quantity,i_quantity,a,b,k))
    
    return total_quantity, price, i_quantity, i_profit

def demand(a,b,q):
    """ solve for inverse demand of total production

        Args:
            a (symbol): demand parameter
            b (symbol): demand elasticity
            q (symbol): produced qauntity in total

        Returns:
            result (RootResults): the solution represented as a RootResults object

    """ 
    return (a-b*q)

def perfect_com(qi,N,a,b,k):
    """ solve for the produced quantity under the assumption of perfect competition

        Args:
            qo (symbol): produced qauntity by firm 0
            qi (symbol): produced qauntity by firm i
            a (symbol): demand parameter
            b (symbol): demand elasticity
            k (symbol): marginal cost of production 

        Returns:
            result (RootResults): the solution represented as a RootResults object

    """ 
    pc_quantity = sm.solve(sm.Eq(diff(cost_f(qi,k),qi), p_total(0,qi,a,b)),qi)
    return pc_quantity

def plot_deadweight_loss(N,a,b,k):
    """ solves the cournot model and plots the solution showing the deadweight loss

        Args:
            N (symbol): The number of firms in the modl
            a (symbol): demand parameter
            b (symbol): demand elasticity
            k (symbol): marginal cost of production

        Returns:
            result (RootResults): the solution represented as a RootResults object

    """ 
    
    qi = sm.symbols('q_i') #quantity of the N firm 
    plt.rcdefaults()

    pc_quantity = perfect_com(qi,N,a,b,k)
    #pc_price = p_total(pc_quantity[0]/2,pc_quantity[0]/2,a,b)
    produced_quantity = solution_cournot(N,a,b,k)[0]

    data = np.arange(0,pc_quantity[0]+5,1)  # use numpy to create a range of data

    marginalcost = np.zeros(len(data))
    for i in data:
        marginalcost[i] = diff(cost_f(qi,k),qi).subs({qi:data[i],k:k})  

    plt.xlabel("Quantity") # label the axes
    plt.ylabel("Price") # label the axes

    plt.annotate('PC equilibrium', xy=(pc_quantity[0],1.5))
    plt.annotate('Demand', xy=(1,a))
    plt.annotate('MC', xy=(1.8,1.5))
    plt.annotate('Produced quantity', xy=(produced_quantity,a))

    plt.plot(data,demand(a,b,data))
    plt.plot(data,marginalcost)
    plt.vlines(x=produced_quantity,ymin=0,ymax=a)

    
    
    
    return plt.show()