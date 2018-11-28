import sqlite3
import sqlalchemy
import click
from flask import current_app, g
from flask.cli import with_appcontext
from sqlalchemy import *

class Dbconnect:
    def __init__(self):
        self.engine=create_engine('sqlite:///../instance/Rooms.db')

    def get_engine(self):
        return self.engine
    def dispose_engine(self):
        self.engine.dispose()

def load_floor_context (dbengine, building, floor):
    engine=dbengine.get_engine()
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
    conn.close()

    return dic

def get_floors(dbengine,building):

    engine=dbengine.get_engine()
    conn = engine.connect()
    floors=[]
    cor = conn.execute("SELECT DISTINCT floor FROM locations WHERE building = ?", building)
    for row in cor:
        floors.append(str(row[0]))
    conn.close()
    return floors

def get_floor(dbengine,name):

    engine = dbengine.get_engine()
    conn = engine.connect()
    node = name.lower()
    cor = conn.execute("SELECT floor FROM locations WHERE name = ?", name)
    floor = []
    for row in cor:

        floor.append(str(row[0]))
    conn.close()


    return str(floor[0])

def get_node(dbengine,name):
    engine = dbengine.get_engine()
    conn = engine.connect()
    node = name.lower()
    cor = conn.execute("SELECT location_id FROM locations WHERE name = ?", name)
    floor = []
    for row in cor:

        floor.append(str(row[0]))
    conn.close()


    return str(floor[0])

def get_building(dbengine,name):

    engine = dbengine.get_engine()
    conn = engine.connect()
    cor = conn.execute("SELECT building FROM locations WHERE name = ?", name)
    building = []
    for row in cor:

        building.append(str(row[0]))
    conn.close()


    return str(building[0])

def load_stair_context (dbengine, building,end_floor):
    engine=dbengine.get_engine()
    conn = engine.connect()
    cor = conn.execute("SELECT * FROM locations WHERE building = ?  AND type = 'stair' ", building)
    dic = {}
    dic['config'] = {}
    dic['config']['flag']='no'
    for row in cor:
        indic={}
        inlist=[]
        dic[row[0]]=indic
        indic ['sig']='no'
        indic['floor'] = str(row[4])
        indic['x'] = row[5]
        indic['y'] = row[6]
        for z in range (7,14):
            if row[z] is None:
                break
            inlist.append(row[z])
        indic['edges'] = inlist
    conn.close()

    for node in dic:

        if (node=='config')==False:

            thisfloor=dic[node]['floor']
            if thisfloor==end_floor:
                dic[node]['sig']='goal'
            #prune non stair edges
            for edge in dic[node]['edges']:
                if (edge in dic)==False:
                    dic[node]['edges'].remove(edge)








    return dic




