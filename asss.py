name= ['john','jacob','anabel','jonathan','jack','tabitha','winifred','jalang']
# Starts with J
for i in name:
    if i[0] == 'j':
       print ('{} = True'.format(i))
    else:
        print ('{} = False'.format(i))

print()

#longest name
print('The Longest name in the list is = {} '.format(max(name)))

print()
#to sort and index
 
name.sort()
for i, string in enumerate(name):
    print ('{}  :  {}'.format(i, string))

 
print()
# length of all name
for h in name:        
    print ('{} = {} '.format(h,len(h)))
print ()
# Length of list
print ('Length of list is = ',len(name))

print()
#lenght even and old
for i in name:
    if len(i) % 2 == 0:
        print('{} = Even'.format(i))
    elif len(i)% 2 != 0:
        print('{} = Old '.format(i))

print()
    
