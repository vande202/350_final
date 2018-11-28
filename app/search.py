from app.helper import getTestContextMap
import collections
import heapq
import math


class contexGraph:
    def __init__(self,contexMap):
        self.edges={}
        self.flag=contexMap['config']['flag']
        self.solved=False
        self.came_from={}
        self.contexMap=contexMap
        #self.start=contexMap['config']['start']
        self.start,self.goals=self.setGoals(contexMap)
        self.end = 'None'

        for x in contexMap:
            if (x == 'config') == False:
                self.edges[x] = contexMap[x]['edges']

    def neighbors(self,id):

        canditade_edges=self.edges[id]
        edges=[]
        for edge in canditade_edges:
            if (edge in self.contexMap):
                edges.append(edge)
            else:
                print("non-fatal error: "+id+"  has called: "+ edge+"  which does not exist as a key in the graph")




        return edges

    def set_came_from(self,came_from):
        self.came_from=came_from

    def cost(self,current,next):

        try:
            x_c= int(self.contexMap[current]['x'])
            y_c = int(self.contexMap[current]['y'])

            x_n=int(self.contexMap[next]['x'])
            y_n = int(self.contexMap[next]['y'])
            cost= math.sqrt( (x_n - x_c)**2 + (y_n - y_c)**2 )

            return cost
        except :
            return -1


    def set_end(self,end):
        self.end=end

    def isGoal(self,state):
        if state in self.goals:
            return (True)
        else:
            return False




    def setGoals(self,contexMap):
        goal=[]
        start=''

        for node in contexMap:
            if (node=='config')==False:

                if contexMap[node]['sig']=='start':
                    start=node

                if contexMap[node]['sig']=='goal':
                    goal.append(node)


        return start,goal

    def heuristicCost(self,current):

        closeestgoal=''
        thiscost=0
        goalcost=-1

        for goal in self.goals:
            thiscost=self.cost(goal,current)
            if thiscost<goalcost or (goalcost==-1):
                goalcost=thiscost
                closeestgoal=goal


        finalcost=goalcost*3
        return finalcost


class PriorityQueue:

    def __init__(self):
        self.elements=[]

    def empty(self):
        return len(self.elements)==0

    def put (self,item,priority):
        heapq.heappush(self.elements,(priority,item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def a_star_search(graph):

    end='nothing'
    start=graph.start


    frontier=PriorityQueue()
    frontier.put(start,0)
    came_from={}
    cost_so_far={}
    came_from[start]=None
    cost_so_far[start]=0

    while not frontier.empty():
        current=frontier.get()

        if graph.isGoal(current)==True:
            graph.set_came_from(came_from)
            graph.solved=True
            graph.set_end(current)
            break

        for next in graph.neighbors(current):
            cost1=graph.cost(current,next)
            if cost1>0:

                new_cost=cost1+cost_so_far[current]

                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next]=new_cost
                    priority=new_cost+graph.heuristicCost(next)
                    frontier.put(next,priority)
                    came_from[next]=current
            else:
                print(next)


    return graph
