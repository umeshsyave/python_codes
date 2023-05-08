christmas_tree= [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,1,1,1,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
def tree():
    for item in christmas_tree:
        for item1 in item:
            if item1==0:
                print(' ',end='')
            elif item1==1:
                print('*',end='')
        print('')

for x in list(range(0,10)):
    tree()

