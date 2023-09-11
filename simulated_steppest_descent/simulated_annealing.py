import math as m
import random as r

class HC_Simulated_Annealing:
    '''
    This class will sort an unsorted list using Hill Climbing (Simulated Annealing) local search
    '''

    def __init__(self, lst):
        '''
        This constructor will take input a python list as a parameter
        and store the list to a class instance variable
        '''
        self.mainlst = lst
        print(self.mainlst)

    def calc_cost(self, lst):
        '''
        This class method will take input a python list as a parameter
        and will count the total number of conflicts within this list and return the count.

        A conflict is a pair of integers in wrong order.
        For example:
        In [4,1,3,2] => (4,1), (4,3), (4,2), (3,2) are 4 conflicts.

        Hint: for each element of the list compare it with the rest of the elements of that list.
        '''
        cost = 0
        for index in range(0, len(lst)):
            eachitem = lst[index]
            for nextindex in range(index + 1, len(lst)):
                nextitem = lst[nextindex]
                if (nextitem < eachitem):
                    cost = cost + 1
        return cost

    def random_child(self, lst):
        index1 = r.randint(0, len(lst)-1)
        index2 = r.randint(0, len(lst)-1)
        # print(index1,index2)
        temp_lst = lst.copy()
        temp_lst[index1], temp_lst[index2] = temp_lst[index2], temp_lst[index1]
        return temp_lst
        '''
        This class method will take input a python list (e.g. lst) as a parameter
        and will generate a random child list by swaping any two random list elements.

        Randomly select two different indices of the list using random.randrange(0,len(lst))
        and swap them and return the new list.

        Hint: a, b = b, a ; direct swap operation in python. For example, lst[i], lst[j] = lst[j], lst[i]

        Hint: Remember list works like pass by reference.
              So make sure to use a copy of the list by using list.copy() method where necessary
              instead of changing the main list.
        '''
    # def curtemp(self, time):
    #     return init
    def SimulatedAnnealing(self):
        current_lst = self.mainlst
        current_cost = self.calc_cost(current_lst)
        initial_temp = 100
        time = 1
        while time<m.inf:
            mytemp = initial_temp-0.01*time
            # print(mytemp)
            if mytemp <= 0 :
                break
            random_child = self.random_child(current_lst)
            random_child_cost = self.calc_cost(random_child)
            if random_child_cost < current_cost:
                current_cost = random_child_cost
                current_lst = random_child
            else:
                energy = random_child_cost - current_cost
                prob = m.exp(-energy/mytemp)
                rand = r.random()
                # print(rand)
                if rand < prob:
                    current_cost = random_child_cost
                    current_lst = random_child
                else:
                    continue
            time = time+1
        return current_lst
        '''
        1) Set the class instance variable list (set in the __init__() step) as the "current list".
        2) Calculate the "current cost" using the self.calc_cost() function on the "current list".

        3) Set the "initial temperature" value to 100 in a temperature variable
        4) Declare a while loop where a time variable will start iterating from 1 to infinity
           and within the while loop do the followings:
            - Calculate the current temperature value using the function,
                      Current Temp=initial temperature-0.01*time
            - If the current temperature is zero or less then stop the while loop
            - Otherwise
                -  find out the "next child" by calling the self.random_child(current list) method
                -  calculate the "next child cost" by using the self.calc_cost(next child) method
                -  calculate the difference between the next child cost and the current cost value
                -  if the next child cost is less than the current cost then
                   update the current cost and current list as the next child list and next child cost
                -  otherwise, generate a random number between (0,1) and
                              check whether it is less than e^(-(cost difference)/current temperature)
                              - If yes, then update the current list and current cost as the next child list and next child cost
                              - Otherwise do nothing

        4) return the current list
        '''

#If your class implementation is correct then the following code will work properly
mylist=[100,-50,8,10,-20,200,50]
ob=HC_Simulated_Annealing(mylist)
result=ob.SimulatedAnnealing()
print(result) #your final output can be optimal / suboptimal