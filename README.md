TO DO:

x1. build tests for lineup.py

X2. finish lineup.py

X3. build tests for pool.py

X4. finish pool.py

5. build and test basic optimizer.py

6. build and test rust version of basic optimizer

7. build and test python genetic optimizer

8. port genetic optimizer to rust

9. benchmark everything

10. profit




pseudo code for a genetic algorithm

credit to this great walkthrough for Genetic Algorithms https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_quick_guide.htm
credit to this great lecuture from Patrick Winston on Genetic Algorithms https://www.youtube.com/watch?v=kHyNqSnzP8Y
credit to https://github.com/DimaKudosh/pydfs-lineup-optimizer/
credit to this repository https://github.com/DimaKudosh/pydfs-lineup-optimizer/blob/master/pydfs_lineup_optimizer/lineup_optimizer.py


Function GA

   initialize population

   find fitness of population
   
   while (termination criteria is reached) do

      parent selection

      crossover with probability pc

      mutation with probability pm

      decode and fitness calculation

      survivor selection

      find best

   return best

BASIC HEURISTIC for first attempt

each gene is player pool which is a subset of the entire player pool

we use the dynamic programming solution to find the optimal lineup for the subset

	for draftkings we may or may not allow the entire playerpool to be available for flex

we use a roullette wheel using rank bias to select parents

we combine the genes via combining the playerpools and randomly choosing a new playerpool

	we bias based on if the player was in 1 or both optimals

we will attempt to introduce mutations via adding 1 random player to each playerpool

we will have elitism via always having 1 playerpool contain all the members of the

	top 2 to 3 optimal lineups

we will terminate the process after a certain number of generations.

the reason for never terminating faster is to provide users of this consistency

in how long they can expect the algorithm to take.


TASKS

X - Set up PlayerPool

1. set up the FullOptimizer class


Method- 

- Test that the playerpool is valid

- lock in the locks/remove locks from playerpool

-begin a while loop to produce multiple players

-update current exposures

-use current exposures to update player pool

