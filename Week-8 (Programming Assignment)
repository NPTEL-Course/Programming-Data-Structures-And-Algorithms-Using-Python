R,C,K,D=input().split()
D=int(D)
R=int(R)
K=int(K)
C=int(C)
Dragon_position=list()
distance=0
store=dict()
for g in range(D):
        x,y=input().split()
        x=int(x)
        y=int(y)
        Dragon_position.append([x,y])
#print(Dragon_position)
ans=9999999
from itertools import combinations
comb = combinations(Dragon_position, K)
list_comb=list()
for i in list(comb):
    list_comb.append(sorted(i))
    #print(sorted(i))
#print(list_comb)
dragon_initial_position=[0,0]
store=dict()
for row in list_comb:
    for column in range(len(row)):
         if row[:column+1] in store.values():
             sub_part_list = row[:column + 1]
             p=sub_part_list[len(sub_part_list) - 1:len(sub_part_list)]
             #print("p=",p)
             distance=list(store.keys())[list(store.values()).index(row[:column+1])]
             dragon_initial_position[0] = p[0][0]
             dragon_initial_position[1] = p[0][1]
             #print("went for dynamic")
         else:
            r=row[column][0]
            c=row[column][1]
            distance = distance + abs(dragon_initial_position[0] - r) + abs(dragon_initial_position[1] - c)
            dragon_initial_position[0] = r
            dragon_initial_position[1] = c
            sub_part=[]
            sub_part=row[:column+1]
            store[distance]=sub_part
            #print("sublist = ",store[distance],"subintial = ",sub_part[len(sub_part)-1:len(sub_part)])
        #print(distance)
        #previous_distance = distance
    if ans>distance:
        ans=distance
    distance=0
    dragon_initial_position[0] = 0
    dragon_initial_position[1] = 0
print(ans)
