from app.helper import getTestContextMap
from app.helper import gettestAOM
import app.helper as helper
import app.search as search
import app.mapTools as mT
import app.test as test
import app.db as db

def the_magic_machine(start_str,end_str):
    AOM = getBaseAOM(start_str, end_str)
    AOM=add_all_to_AOM(AOM,start_str,end_str)



    return AOM

def build_test_base_context(start,end):
    ContexMap = helper.getTestContextMap()
    flag=ContexMap['config']['flag']
    del ContexMap['config']

    ContexMap['config']={'flag':flag}

    ContexMap[start]['sig']='start'
    ContexMap[end]['sig'] = 'goal'
    return ContexMap

def add_all_to_AOM(AOM,start,end):
    # start the database engine
    dbengine = db.Dbconnect()


    # get the names
    start_node=db.get_node(dbengine,start)
    end_node=db.get_node(dbengine,end)

    #tell me where my start and end points are
    start_building=db.get_building(dbengine,start)
    start_floor=db.get_floor(dbengine, start)
    end_floor=db.get_floor(dbengine, end)
    end_building=db.get_building(dbengine,end)

    #start at the start floor
    current_floor=start_floor
    current_building=start_building

    #set current node to start node
    current_node=start_node


    #while until current_floor=end_floor



    #loop for the building
    while (True):
        #goal saits for this floor are calculated
        stairs = db.load_stair_context(dbengine, current_building, current_floor)

        #base direction, will determine if stair goals or end_node is used as goal
        direction=0
        if int(end_floor)>int(current_floor):
            #direction UP, dirty but it works
            direction=1
        if int(end_floor)<int(current_floor):
            #direction Down
            direction=-1

        new_stairs,goal_stairs=mT.get_goal_stairs(stairs,direction,current_floor)


        #ADD CURENT FLOOR BLOCK, yes i know its messy im tired and im dont CARE anymore


        # raw contex from floor
        raw_contex_map = db.load_floor_context(dbengine, current_building, current_floor)

        #get goals, and refine the context map accordingly
        if len(goal_stairs)==0:
            contex_map = mT.set_contex_map_flag_start_goal(raw_contex_map, current_floor, current_node,[end_node] )
        else:
            contex_map = mT.set_contex_map_flag_start_goal(raw_contex_map, current_floor, current_node, goal_stairs)

        # refined context given end and current/ last floors

        # modeling
        contex_graph = search.contexGraph(contex_map)
        #solving the model
        solved_graph = search.a_star_search(contex_graph)


        #add floor to AOM
        AOM = mT.add_floor(AOM, current_building, current_floor, 1)

        #add reddots on all
        #AOM = mT.add_dot_on_all_nodes_to_AOM(AOM, contex_graph, end_floor, 1)

        #add start and end
            #end
        if (len(goal_stairs)==0)==False:
            this_end_node =solved_graph.end
            this_end_node_destination=stairs[this_end_node]['edges'][0]
            this_end_node_pointer=stairs[this_end_node_destination]['floor']


            AOM=mT.add_dot_on_this_node_to_AOM(AOM,contex_map,this_end_node,current_floor,this_end_node_pointer,2)

        #add the path
        AOM = mT.add_path_to_AOM(AOM, solved_graph, 1)


        #CRITICAL break statement
        if (current_floor==end_floor):
            break

        # update current_floor, God help us all, THE UPDATE IS AFTER THE BREAK CHECK, so the end_floor is also done
        print(solved_graph.end)

        current_node=stairs[solved_graph.end]['edges'][0]
        current_floor=stairs[current_node]['floor']
        print('yays')

    AOM=mT.set_AOM_stateflag(AOM,start_floor)









    #TESTING SECTION:

    #TESTING END



    #add building portals
    #TODO



    #close endgine

    dbengine.dispose_engine()
    return AOM



def build_dbtest_base_context(start,end):
    dbengine = db.Dbconnect()


    start_building=db.get_building(dbengine,start)
    start_floor=db.get_floor(dbengine, start)
    end_floor=db.get_floor(dbengine, end)
    end_building=db.get_building(dbengine,end)

    if (end_building==start_building):
        print('yay')
        print(db.load_stair_context(dbengine,start_building,start_floor,end_floor))

    if (end_building == start_building)==False:
        print('shit, wrong building')


    ContexMap=db.load_floor_context(dbengine,start_building,start_floor)
    start_building_floors=db.get_floors(dbengine,start_building)


    ContexMap['config']['flag']='Ground'
    ContexMap['rs108']['sig'] = 'goal'
    ContexMap['stg1U']['sig'] = 'start'
    #print(ContexMap)

    return ContexMap

def getBaseAOM(start,end):
    AOM = gettestAOM()


    return AOM
