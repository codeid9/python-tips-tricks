from operator import itemgetter

names = [('Ben','John'),('Peter','Parker'),('Kelly','Isa')]

# sort by first name
sorted_names = sorted(names,key=itemgetter(0))
print('Sorted by first name:',sorted_names)
# use index 1 if you want to sort by last name

# sort by first name then last name
sort_names = sorted(names,key=itemgetter(0,1))
print('Sorted by first name & last name:',sort_names)