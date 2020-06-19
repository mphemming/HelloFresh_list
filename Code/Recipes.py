#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:46:43 2020

@author: Michael
"""
# %% -----------------------------------------------------------------------------------------------
# Import modules

import numpy as np
from collections import Counter
from itertools import compress

# %% -----------------------------------------------------------------------------------------------
# Shopping list

class BangBangCauliflower:
    recipe = []
    recipe = ['cauliflower-2', 
              'mayonnaise-200-g',
              'olive oil',
              'sweet chilli sauce-200-g',
              'panko breadcrumbs',
              'salt',
              'garlic-4-cloves',
              'butter-40-g',
              'jasmine rice',
              'water',
              'Asian greens-2-bunches',
              'carrot-2',
              'spring onion-1-bunch',
              'rice wine vinegar',
              'soy sauce']
   
class IndianChickpeaPatties:    
    recipe = []
    recipe = ['olive oil',
              'potato-4',
              'chickpeas-2-tins',
              'carrot-2',
              'cucumber-2',
              'cherry tomatoes-2-punnets',
              'coriander-1-bag',
              'red onion-0.5',
              'lime-1',
              'egg-2',
              'mango chutney-100-g',
              'fine breadcrumbs',
              'mumbai spices',
              'mayonnaise-200-g']
    
class IndianSalmonBombayPotatoes:
    recipe = []
    recipe = ['olive oil',
              'potato-4',
              'salt',
              'turmeric-0.5-sachet',
              'brown mustard seeds-2-sachet',
              'garlic-4-cloves',
              'greek yoghurt-200-g',
              'coriander-1-bag',
              'cucumber-2',
              'tomato-2',
              'white wine vinegar-1-tbs',
              'mixed salad leaves-60-g',
              'mild north indian spice blend',
              'salmon-4']
    
class SweetChilliTofuSesameNoodles:
     recipe = []
     recipe = ['olive oil',
              'garlic-4-cloves',
              'capsicum-2',
              'zucchini-2',
              'carrot-2',
              'malaysian tofu-2-blocks',
              'udon noodles-2-packets',
              'sweet chilli sauce-100-g',
              'soy sauce-1-tbs',
              'dark roasted peanut butter-2-packets',
              'soy sauce-0.25-cup',
              'sesame oil blend-30-g',
              'brown sugar-2-tsp',
              'crushed peanuts-2-packets']
    
class CreamyMushroomCherryTomatoSpaghetti:
     recipe = []
     recipe = ['olive oil',
               'cherry tomatoes-2-punnets',
               'balsamic vinegar-2-tbs',
               'brown sugar-2-tbs',
               'spaghetti-2-packets',
               'garlic-6-cloves',
               'panko breadcrumbs-1-packet',
               'sliced mushrooms-300-g',
               'butter-40-g',
               'light thickened cream-300-ml',
               'vegetable stock-2-cubes',
               'grated parmesan cheese-60-g',
               'basil-1-punnet',
               'baby spinach leaves-120-g']
    
    
    
    
   
    
# %% -----------------------------------------------------------------------------------------------
# functions   
    
def sort_ingredients(combined_list):
    
    # separate into item and quantity groups
    item = []
    quantity = []
    quantity_numeric = []
    units = []
    for items in range(len(combined_list)):
        split =  combined_list[items].split('-')
        item.append(split[0])
        if len(split) > 1:
            quantity.append(split[1]) 
            quantity_numeric.append(float(split[1]))             
        else:
            quantity.append(' ')  
            quantity_numeric.append(np.nan)
        if len(split) > 2:
            units.append(split[2]) 
        else:
            units.append(' ')              
            
    # calculate total quantities
    how_many = {}
    for items in range(len(combined_list)):
         how_many[item[items]] = item.count(item[items])
    # identify duplicates
    duplicates = [k for k,v in Counter(item).items() if v>1]
    # match quantities to items
    quantity_total = quantity
    for n_dups in range(len(duplicates)):
        index = []
        for items in range(len(combined_list)):
            if duplicates[n_dups] in item[items]:
                index.append(True)
            else:
                index.append(False)
                
        positions = [i for i, x in enumerate(index) if x]  
        # get sum
        for n_pos in range(len(positions)):
            if n_pos == 0:
                quantity_sum = quantity_numeric[positions[n_pos]]
            else:
                quantity_sum = quantity_sum + quantity_numeric[positions[n_pos]]      
        # add sum to list
        for n_pos in range(len(positions)):
            quantity_total[positions[n_pos]] = quantity_sum             
        # create string list
        item_list = []
        for items in range(len(combined_list)):
            str_item = item[items] + ' ' + str(quantity_total[items]) + \
                             ' ' + units[items]
            str_item.replace('nan','')
            item_list.append(str_item)
    item_list = set(item_list)
    
    return item_list
        
        
        
        
        
        
        
        
        

    
        
    
    
    
        