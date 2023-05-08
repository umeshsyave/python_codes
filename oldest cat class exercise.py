# finding oldest cat using class functionality by object oreinted programming
cat_list=[]
class cat:
    species='mammal'
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        cat_list.append(age)

cat1=cat('pinky', 6)
cat2=cat('tom', 4)
cat3=cat('sunny', 7)

print(f'oldes cat is {max(cat_list)} years old')

#def oldest(*args):
 #   return(max(args))

#print(f'theoldest cat is {oldest(cat1.age,cat2.age,cat3.age)} years old ')