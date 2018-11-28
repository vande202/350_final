import app.helper as helper

#AOM addition functions
def add_dot_on_all_nodes_to_AOM(AOM,solved_graph,pointer,stack):

    ContexMap=solved_graph.contexMap
    flag=solved_graph.flag
    for x in ContexMap:
        if (x=='config')==False:
            newobject={}
            newobject['type']='reddot'
            newobject['flag']=flag
            newobject['pointer']=pointer
            newobject['stack'] = stack
            newobject['width'] = 10
            newobject['height'] = 10
            newobject['x_cord'] = int(ContexMap[x]['x'])-int(10/2)
            newobject['y_cord'] = int(ContexMap[x]['y'])-int(10/2)


            AOM.append(newobject)


    return AOM

def add_dot_on_this_node_to_AOM(AOM,ContexMap,node,flag,pointer,stack):
    newobject = {}
    newobject['type'] = 'reddot'
    newobject['flag'] = flag
    newobject['pointer'] = pointer
    newobject['stack'] = stack
    newobject['width'] = 10
    newobject['height'] = 10
    newobject['x_cord'] = int(ContexMap[node]['x']) - int(10 / 2)
    newobject['y_cord'] = int(ContexMap[node]['y']) - int(10 / 2)
    AOM.append(newobject)

    return AOM

def add_path_to_AOM(AOM,Contextgraph,stack):
    ContexMap=Contextgraph.contexMap
    came_from=Contextgraph.came_from


    flag=ContexMap['config']['flag']
    startnode = Contextgraph.start
    endnode=Contextgraph.end
    x_last = ContexMap[endnode]['x']
    y_last = ContexMap[endnode]['y']


    def trace_back(AOM,came_from,this,x_last,y_last):
        previous=came_from[this]
        newobject = {}


        x_new = ContexMap[previous]['x']
        y_new = ContexMap[previous]['y']


        newobject['type'] = 'line'
        newobject['flag'] = flag
        newobject['stack']=stack
        newobject['x_origin'] = int(x_last)
        newobject['y_origin'] = int(y_last)
        newobject['x_destination'] = int(x_new)
        newobject['y_destination'] = int(y_new)

        x_last=x_new
        y_last=y_new

        AOM.append(newobject)
        return AOM,previous,x_last,y_last

    precedent=endnode

    while (precedent==startnode)==False:
        AOM,precedent,x_last,y_last=trace_back(AOM,came_from,precedent,x_last,y_last)



    return AOM


def add_floor(AOM,building,floor,stack):

    srcs=helper.get_image_srcs()
    src=srcs[building][floor]
    print (src)
    newobject = {}
    newobject['type'] = 'image'
    newobject['flag'] = floor
    newobject['src']=src
    newobject['pointer'] = 'none'
    newobject['stack'] = stack
    newobject['width'] = 1000
    newobject['height'] = 1000
    newobject['x_cord'] = 0
    newobject['y_cord'] = 0

    AOM.append(newobject)


    return AOM

def set_AOM_stateflag(AOM,newflag):
    j=0
    for i in AOM:
        if i['type']=='config':
            AOM[j]['stateflag']=newflag

        j=j+1

    return AOM


#interior helper functions
def set_contex_map_flag_start_goal(contex_map,flag,start,goals):

    contex_map[start]['sig'] = 'start'
    contex_map['config']['flag']=flag

    for goal in goals:
        contex_map[goal]['sig'] = 'goal'




    return contex_map

def get_goal_stairs(stairs,direction,current_floor):

    goal_stairs = []
    new_stairs={}
    for candidate_stair in stairs:
        if (candidate_stair == 'config') == False:
            if stairs[candidate_stair]['floor'] == current_floor:
                this_edge = stairs[candidate_stair]['edges'][0]
                if (int(stairs[this_edge]['floor']) == direction + int(current_floor)):
                    goal_stairs.append(candidate_stair)
                    new_stairs[candidate_stair]=stairs[candidate_stair]



    return goal_stairs,new_stairs

