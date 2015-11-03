'''
Created on 2015. 11. 3.

@author: User
'''
import pickle
import nester


new_man = []

try: 
    with open('man_data.txt',  'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('file err ;  ' + str(err))
    
#except pickle.PickleError as perr:
#    print('pickle err :  ' + str(perr))
nester.print_lol(new_man)


'''
with open('mydata.pickle', 'wb') as mysavedata:
    pickle.dump([1,2,'three'], mysavedata)
    
with open('mydata.pickle', 'rb') as mystoredata:
    a_list = pickle.load(mystoredata)
    
print(a_list)
'''