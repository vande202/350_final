from sqlalchemy import *



def loadfloor (building, floor):
    engine = create_engine('sqlite:///../instance/Rooms.db')
    conn = engine.connect()
    cor = conn.execute("SELECT * FROM locations WHERE building = ?  AND floor = ? ", building, floor)
    dic = {}
    dic['config'] = {}
    dic['config']['flag']='no'
    for row in cor:
        indic={}
        inlist=[]
        dic[row[0]]=indic
        indic ['sig']='no'
        indic['x'] = row[5]
        indic['y'] = row[6]
        for z in range (7,14):
            if row[z] is None:
                break
            inlist.append(row[z])
        indic['edges'] = inlist
    return dic







