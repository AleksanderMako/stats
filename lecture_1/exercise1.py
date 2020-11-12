import numpy as np 
from fractions import Fraction

# experiment configs
outcome_space = [1,2,3,4,5,6]
iterations = 100000

# experiment simulator 
def simulate(event_a, event_b,experiment_iterations):

    intersection = (set(event_a) & set(event_b))
    timesFound =0
    for _ in range(experiment_iterations):

        #draw
        dice = np.random.randint(1,7)
        if dice in intersection:
            timesFound+=1
    
    probability = timesFound/experiment_iterations
    return probability


# event A [2,4,6]
# evet B[1,2,3,4]
# P(A&B) = 1/3
intersection_probability = simulate([2,4,6],[1,2,3,4],iterations)
print('probability of intersection: ',intersection_probability)

# new experiment 
# event A is i roll 2 
# event B is i have rolled even number 

#P(A) = 1/6
p_of_A     = simulate([2],outcome_space, iterations) 
print('probability of rolling 2: ',p_of_A)

#P(B) = 1/2
p_of_B     = simulate([2,4,6],outcome_space,iterations)
print('probability of rolling even: ',p_of_B)

#P(A&B) is the same as P(A) =1/6
p_of_AandB = simulate([2],[2,4,6],iterations)
print('probability of A intersect B: ',p_of_AandB)

#P(A|B) = P(A&B)/P(B)
#       = 1/6  * 2
#       = 1/3

print('probabilit of A|B: ',p_of_AandB/p_of_B)

#P(B|A) is one because 2 is even
print('probability of B|A: ', p_of_AandB/p_of_A) 

