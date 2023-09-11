import math as m
from  queue import PriorityQueue
class PQ_node:
    def __init__(self,nodenumber):
        self.nodenumber = nodenumber
        self.parent = None
        self.actual_cost = m.inf

    def setparent(self,parentobj):
        self.parent=parentobj

    def upadate_cost(self,costval):
        self.actual_cost = costval

#To build priority queue for this object, we need to implement the PriorityItem class as below   >>>in python normally priority queue does't work for object.
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int          #priority based on int.
    item: Any=field(compare=False)


class UCS:
    def buid_adj_list(self,file_name):
        with open(file_name, 'r') as f:  # opening the file with as f. f is the accessing variable.
            firstline = f.readline()  # only one operation with one open.
            print(firstline.split())  # return spliing two value as a string list.
            self.nodes, self.edges, self.goalnode = [int(eachval) for eachval in firstline.split()]  # spliting first two value(no.of.nodes & no.of.edges) in a list then converting eachvalue into int value one by one using for loop
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

    def main_ucs(self, initial_node):
        src_node_object = PQ_node(initial_node)
        src_node_object.setparent(None)      #no parent for initial node or source node.
        src_node_object.upadate_cost(0)         #cost from src_node to src_node is 0

        visited_node = []

        pq = PriorityQueue()                          #making priority object pq
        pq.put(PrioritizedItem(0, src_node_object))      # insert object into priority queue(pq) using Prioritizeditem class object. >>> (cost , obj) >> priority considering cost.

        while not pq.empty():
            popped_item = pq.get()
            popped_node_obj = popped_item.item         #node obj is stored in item key from Prioritizeditem class
            popped_node_number = popped_node_obj.nodenumber

            if popped_node_number == self.goalnode:       #if popped node from priority queue is the goal node : printing the path to goal node and then exit the while.(goal reached)
                goal_node_obj = popped_node_obj
                print("\npath is:", goal_node_obj.nodenumber, end=" ")
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
                    neighbour_node_number = eachneighbour[0]            #from each neighhbour_list first val is node number
                    neighbour_edge_weight = eachneighbour[1]            #2nd value is cost/weight of the edge

                    neighbour_node_obj = PQ_node(neighbour_node_number)
                    neighbour_node_obj.setparent(popped_node_obj)
                    neighbour_node_obj.upadate_cost(popped_node_obj.actual_cost + neighbour_edge_weight)

                    pq.put(PrioritizedItem(neighbour_node_obj.actual_cost, neighbour_node_obj))                     #inserting the neighbour_node_obj into the priority obj_list pq.




obj = UCS()
obj.buid_adj_list("graph.txt")
obj.main_ucs(1)
