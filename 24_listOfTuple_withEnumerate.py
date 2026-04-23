days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

days_tuple = list(enumerate(days,start=1))
print("Method1:",days_tuple)

# methods2
def enum(days,start=1):
    n=start
    for day in days:
        yield n,day
        n+=1
print("Method2:",list(enum(days)))
