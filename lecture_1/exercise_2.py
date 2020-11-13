import numpy as np 
import matplotlib.pyplot as plot 

#simulation configs 
iterations  =100000

#Event heads on first toss
firts_toss_head = lambda c1,c2:c1==1

#Event heads on second toss
second_toss_head = lambda c1,c2:c2==1

#Event snake eyes/same outcome
snake_eyes = lambda c1,c2:c1==c2

#Event two heads
head_head = lambda c1,c2:c1==1 and c2 == 1

#Event two tails 
tail_tail = lambda c1,c2:c1==0 and c2 == 0

#Event head then tail 
head_tail = lambda c1,c2:c1==1 and c2 == 0

#Event tail then head 
tail_head = lambda c1,c2:c1==0 and c2 == 1

#simulation 

def simulation(iterations ,comparator):

    eventFrequency =0
    for _ in range(iterations):
        c1 = np.random.randint(0,2)
        c2 = np.random.randint(0,2)
        if comparator(c1,c2):
            eventFrequency+=1
    
    return eventFrequency/iterations

p_of_first_toss_h  = simulation(iterations,firts_toss_head)
p_of_second_toss_h = simulation(iterations,second_toss_head)
p_of_same          = simulation(iterations,snake_eyes)
p_of_hh            = simulation(iterations,head_head)
p_of_tt            = simulation(iterations,tail_tail)
p_of_ht            = simulation(iterations,head_tail)
p_of_th            = simulation(iterations,tail_head)

print(p_of_first_toss_h)
print(p_of_second_toss_h)
print(p_of_same)
print(p_of_hh)
print(p_of_tt)
print(p_of_ht)
print(p_of_th)


