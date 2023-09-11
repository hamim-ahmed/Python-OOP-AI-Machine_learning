
import math as m

class HillClimbing:
    '''
    This class will sort an unsorted list of integers
    using Hill Climbing (Steepest Descent) local search algorithm
    '''

    def __init__(self, lst):
        '''
        This constructor will take input a python list as a parameter
        and store the list in a class instance variable
        '''
        self.mainlst = lst
        print(self.mainlst)

    def calc_cost(self, lst):
        '''
        This class method will take input a python list as a parameter
        and will count the total number of conflicts within that list and return the count value.

        A conflict is a pair of integers in wrong order.
        For example:
        In [4,1,3,2] => (4,1), (4,3), (4,2), (3,2) are 4 conflicts.

        Hint: for each element of the list compare it with the rest of the elements of that list.
        '''
        cost = 0
        for index in range(0,len(lst)):
            eachitem = lst[index]
            for nextindex in range(index+1,len(lst)):
                nextitem = lst[nextindex]
                if (nextitem<eachitem):
                    cost = cost+1
        return cost



    def minimum_cost_child(self, lst):
        '''
        This class method will take input a list (e.g. lst) as a parameter
        and will generate all possible child lists from the given list (lst)
        by swapping any two elements of the given list.

        For each child list, calculate it's cost by using self.calc_cost() function.

        Track the minimum cost child list and return the minimum cost child list.

        Hint: for each element of the list
              swap it with the rest of the element of the list one by one
              to generate all the child lists.

        Hint: a, b = b, a ; direct swap operation in python. For example, lst[i], lst[j] = lst[j], lst[i]

        Hint: Remember list works like pass by reference.
              So make sure to use a copy of the list by using list.copy() method where necessary
              instead of changing the main list.
        '''
        # temp_lst = []
        min_cost = m.inf
        for index in range(0,len(lst)):
            for nextindex in range(index+1,len(lst)):
                temp_lst = lst.copy()
                temp_lst[index], temp_lst[nextindex] = temp_lst[nextindex], temp_lst[index]
                cost = self.calc_cost(temp_lst)
                if cost<min_cost:
                    min_cost = cost
                    l_cost_child = temp_lst

        return l_cost_child



    def SteepestDescent(self):
        '''
        1) Set the class instance variable list (set in the __init__() step) as the "current list".
        2) Calculate the "current cost" using the self.calc_cost() function on the "current list".

        3) Declare a while loop that will loop until the "current cost" value is 0
           and within the while loop do the followings:
            - find out the lowest cost child list from the current list
              by calling the self.minimum_cost_child(current_list) function
            - calculate the lowest cost value by calling the self.calc_cost() function
              on the lowest cost child.
            - if the lowest cost is lower than the current cost value
              then update the current cost and current list to this lowest cost and lowest cost child.

              Otherwise exit from the while loop as no child is better than the current list.

        4) return the current list
        '''
        current_lst = self.mainlst
        current_cost = self.calc_cost(current_lst)
        # print("main cost: \n", current_cost)
        while current_cost!=0:
            l_cost_child = self.minimum_cost_child(current_lst)
            lowest_cost = self.calc_cost(l_cost_child)
            if lowest_cost<current_cost:
                current_cost = lowest_cost
                current_lst = l_cost_child
            else:
                break
        return current_lst




#If your class implementation is correct then the following code will work properly
mylist=[100, -50, 8, 10, -20, 200, 50]
ob=HillClimbing(mylist)
result=ob.SteepestDescent()
print(result) #your final output can be optimal / suboptimal