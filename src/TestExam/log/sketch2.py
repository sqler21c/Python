'''
Created on 2015. 11. 2.

@author: User
'''
try:
    data = open('sketch.txt')
    
    for each_line in data:
        try:
            (rold, line_spoken) = each_line.split(':', 1)
            print(rold, end='')
            print("  said", end='')
            print(line_spoken, end = '')
        except ValueError:
            pass
        
    data.close()
    
except IOError:
    print('data missing')