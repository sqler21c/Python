'''
Created on 2015. 11. 2.

@author: User
'''

import os
if os.path.exists('sketch.txt'):
    data = open('sketch.txt')

    for each_line in data:
        #if each_line.find(':') != -1:
        try:
            (role, line_spoken) = each_line.split(':',1)
            print(role, end= '')
            print('  said', end = '')
            print(line_spoken, end = '')
        except:
            pass   
        
        data.close()
else:
    print('data missing') 