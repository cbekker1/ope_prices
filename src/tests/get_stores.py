# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:23:47 2023

@author: cleof
"""
# pnp Yes
# 'FriendlyGrocerwaverton' yes
# spar Yes
# Game no
# game no
# GAME no
# "London Grocery" no

#%% 
new_var_name = 'ope_df_' + get_keyword_name(product_keyword) + '_' + store
globals()[new_var_name] = ope_df
del new_var_name