#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:57:52 2020

@author: Michael
"""

# %% -----------------------------------------------------------------------------------------------
# Import modules

import Recipes as rec
import send_email as se
import numpy as np
from collections import Counter
from itertools import compress

# %% -----------------------------------------------------------------------------------------------
# combine recipe ingredients

combined_list = rec.BangBangCauliflower.recipe + \
                rec.IndianChickpeaPatties.recipe + \
                rec.CreamyMushroomCherryTomatoSpaghetti.recipe + \
                rec.IndianSalmonBombayPotatoes.recipe + \
                rec.SweetChilliTofuSesameNoodles.recipe

item_list = rec.sort_ingredients(combined_list)

se.send_email(item_list)

