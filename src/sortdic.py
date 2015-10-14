#sortdic.py
dic={}
list=['is','too','short','life','you','need','python']

j=0
for i in list:
  j=j+1
  dic[i]=j
  
sortKey=dic.keys()
sortKey.sort()

for key in sortKey:
  print key,'\t:', dic[key]
print '='*50

sortValue=dic.values()
sortValue.sort()
for value in sortValue:
  for key in dic.keys():
    if dic[key] == value:
      print "value %s's key is %s" %(value,key)
      
print dic    
      