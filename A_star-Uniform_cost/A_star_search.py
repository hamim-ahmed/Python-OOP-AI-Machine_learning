import math as m
from queue import PriorityQueue
class PQ_node:
    def __init__(self,nodenumber):
        self.nodenumber = nodenumber
        self.parent = None
        self.actual_cost = m.inf       #actual total_cost for a node.
        self.heuristic = m.inf
        self.total_cost = m.inf        #huristic cost + actual_total_cost.

    def setparent(self, parentobj):
        self.parent = parentobj

    def upadate_cost(self,costval):
        self.actual_cost = costval

    def set_heuristic(self,heuristic):
        self.heuristic = heuristic

    def update_total_cost(self):
        self.total_cost = self.actual_cost + self.heuristic

#To build priority queue for this object, we need to implement the PriorityItem class as below   >>>in python normally priority queue does't work for object.
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int          #priority based on int.
    item: Any=field(compare=False)


class A_Star:
    def buid_adj_list(self,file_name):
        with open(file_name, 'r') as f:  # opening the file with as f. f is the accessing variable.
            firstline = f.readline()  # only one operation with one open.
            print(firstline.split())  # return spliting two value as a string list.
            self.nodes, self.edges, self.goalnode = [int(eachval) for eachval in firstline.split()]  # spliting first two value(no.of.nodes & no.of.edges & no.of.goalnode) in a list then converting eachvalue into int value one by one using for loop
            print(self.nodes, self.edges,self.goalnode)
            # print([500]*10)  #500 will be print 10 times in a the list.

            self.adj_list = [[] for eachrow in range(0, self.nodes + 1)]  # for every node(as a index) declearing a empty list([]) to store all the adjacency nodes in them.

            print("connection:")
            for eachline in range(self.edges):
                nextline = f.readline()  # will start from second line....first line already read once.
                firstval, secondval, weight = [int(eachval) for eachval in nextline.split()]
                print("node:", firstval, "to", "node:", secondval)

                self.adj_list[firstval].append([secondval, weight])  # connected node and weight as a list every time for connected nodes.
                # adj_list[secondval].append([firstval, weight])  # as undirected graph.

            print("Final constructed list:")
            for node in range(1, self.nodes + 1):
                print(node, self.adj_list[node])

            lastline = f.readline()
            self.heuristic_values = [0]                     #reading all heuristic value into a list.>> index no 0 is ignored as nodes/vertices starts from 1
            for eachval in lastline.split():
                temp = int(eachval)
                self.heuristic_values.append(temp)          #fill up heuristic list >> starts from index no 1.
            print(self.heuristic_values)

    def main_A_star(self, initial_node):
        src_node_object = PQ_node(initial_node)      #setting the node number
        src_node_object.setparent(None)      #no parent for initial node or source node.
        src_node_object.upadate_cost(0)         #cost from src_node to src_node is 0
        src_node_object.set_heuristic(self.heuristic_values[initial_node])      #setting the heuristic value for the node.obj
        src_node_object.update_total_cost()

        visited_node = []

        pq = PriorityQueue()                          #making priority object pq
        pq.put(PrioritizedItem(0, src_node_object))      # insert object into priority queue(pq) using Prioritizeditem class object. >>> (cost , obj) >> priority considering cost.

        while not pq.empty():
            popped_item = pq.get()
            popped_node_obj = popped_item.item         #node obj is stored in item key from Prioritizeditem class
            popped_node_number = popped_node_obj.nodenumber

            if popped_node_number == self.goalnode:       #if popped node from priority queue is the goal node : parintting the path to goal node and then exit the while.(goal reached)
                goal_node_obj = popped_node_obj
                print("\nfinal path is:", goal_node_obj.nodenumber, end=" ")
                while goal_node_obj.parent is not None:
                    print("<", goal_node_obj.parent.nodenumber, end=" ")
                    goal_node_obj = goal_node_obj.parent
                break

            if popped_node_number in visited_node:
                continue
            else:
                visited_node.append(popped_node_number)
                neighbours_list = self.adj_list[popped_node_number]        #getting all the neighbour list/adjacency list for the popped_node_number(node) >>> exmp: for node_number 1 list will be: [[2, 4], [6, 3]] >>from graph

                for eachneighbour  in neighbours_list:
                    neighbour_node_number = eachneighbour[0]            #first val is node number
                    neighbour_edge_weight = eachneighbour[1]            #2nd value is cost/weight of the edge

                    neighbour_node_obj = PQ_node(neighbour_node_number)    #making new node_obj of neighbours using their node_number
                    neighbour_node_obj.setparent(popped_node_obj)           #keeping the popped_obj into neighbours self.parent for accessing their parent.
                    neighbour_node_obj.upadate_cost(popped_node_obj.actual_cost + neighbour_edge_weight)     #total actual_cost till now for the neighbours.
                    neighbour_node_obj.update_total_cost()         #updating total cost>>>>f(n)+h(n)

                    pq.put(PrioritizedItem(neighbour_node_obj.total_cost, neighbour_node_obj))                     #inserting the neighbour_node_obj into the priority obj_list pq.




obj = A_Star()
obj.buid_adj_list("graph.txt")
obj.main_A_star(1)
