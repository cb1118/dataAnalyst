# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 07:11:38 2018

@author: cb1118
"""

import math

def binom_dist(size,pos_outcomes,weight=.5):
    x = math.factorial(size) / (math.factorial(size-pos_outcomes)*math.factorial(pos_outcomes))
    y = math.pow(weight,pos_outcomes)
    z = math.pow(1-weight,size-pos_outcomes)
    print(x*y*z)
    

binom_dist(1,1,.9)

    
def set_dict_defaults(kwargs, xkey, def_value):
    if not xkey in kwargs:
        kwargs[xkey] = def_value
    else:
        if not isinstance(kwargs[xkey],bool):
            kwargs[xkey]=def_value
            print('\n** Incorrect data type set for {}.  Default of "{}" was used **\n'.format(xkey,def_value))
        


def bayes_rule(P_x,P_pos_x,P_neg_not_x,**kwargs):

    #call fundtion to make sure type is right and defaults are set
    set_dict_defaults(kwargs, 'pos_calc', True)
    set_dict_defaults(kwargs, 'verbose', False)
 
    #calculate the Bayes Rule values    
    P_not_x = 1 - P_x
    P_neg_x = 1 - P_pos_x
    P_pos_not_x = 1 - P_neg_not_x

    if kwargs['pos_calc']:
        Px_of_x = P_x * P_pos_x
        Px_of_not_x = P_not_x * P_pos_not_x
    else:
        Px_of_x = P_x * P_neg_x
        Px_of_not_x = P_not_x * P_neg_not_x
    
    Px = Px_of_x + Px_of_not_x
    Px_of_x_final = Px_of_x / Px
    Px_of_not_x_final = Px_of_not_x / Px
    
    if kwargs['verbose']:
        if kwargs['pos_calc']:
            ret_value = 'Positive Test Results: \n   {}: {}\n   {}: {}'.format("Positive Probability of Occurence",Px_of_x_final,"Positive Probability of No Occurrence",Px_of_not_x_final)
        else:
            ret_value = 'Negative Test Results: \n   {}: {}\n   {}: {}'.format("Negative Probability of Occurence",Px_of_x_final,"Negative Probability of No Occurrence",Px_of_not_x_final)
        return ret_value
    else:
        return Px_of_x_final, Px_of_not_x_final

print(bayes_rule(0.1,.9,.95,pos_calc=True))


"""
Two important mathematical theorems for working with sampling distributions include:

Law of Large Numbers
Central Limit Theorem
The Law of Large Numbers says that as our sample size increases, the sample mean gets closer to the population mean, but how did we determine that the sample mean would estimate a population mean in the first place? How would we identify another relationship between parameter and statistic like this in the future?

Three of the most common ways are with the following estimation techniques:

Maximum Likelihood Estimation

Method of Moments Estimation)

Bayesian Estimation

Though these are beyond the scope of what is covered in this course, these are techniques that should be well understood for Data Scientist's that may need to understand how to estimate some value that isn't as common as a mean or variance. Using one of these methods to determine a "best estimate", would be a necessity.
'''