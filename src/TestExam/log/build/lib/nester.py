# -*- encoding : utf-8
'''
Created on 2015. 11. 2.

@author: User
'''

def print_lol(this_list):
    for each_item in this_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
