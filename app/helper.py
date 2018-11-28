def gettestAOM():
    AOM=[]
    config={
        'type':'config',
        'stateflag':'1',
        'maxstack':'4'


    }
    testportal={
        'type': "floorportal",
        'flag': '1',
        'name':"rsfloor1",
        'src':"../static/image/rsGround.svg",
        'pointer': '2',
        "stack":3,
        'width':100,
        'height':30,
        'x_cord':150,
        'y_cord':20
    }
    testportal1={
        'type': "floorportal",
        'flag': '1',
        'name':"rsfloor1",
        'src':"../static/image/rsGround.svg",
        'pointer': '3',
        "stack":3,
        'width':100,
        'height':30,
        'x_cord':300,
        'y_cord':20
    }

    testportal2={
        'type': "floorportal",
        'flag': '2',
        'name':"rsfloor1",
        'src':"../static/image/rsGround.svg",
        'pointer': '1',
        "stack":3,
        'width':100,
        'height':30,
        'x_cord':20,
        'y_cord':20
    }
    testportal3={
        'type': "floorportal",
        'flag': '2',
        'name':"rsfloor1",
        'src':"../static/image/rsGround.svg",
        'pointer': '3',
        "stack":3,
        'width':100,
        'height':30,
        'x_cord':300,
        'y_cord':20
    }
    testportal4={
        'type': "floorportal",
        'flag': '3',
        'name':"rsfloor1",
        'src':"../static/image/rsGround.svg",
        'pointer': '1',
        "stack":3,
        'width':100,
        'height':30,
        'x_cord':20,
        'y_cord':20
    }
    testportal5={
        'type': "floorportal",
        'flag': '3',
        'name':"rsfloor1",
        'src':"../static/image/rsGround.svg",
        'pointer': '2',
        "stack":3,
        'width':100,
        'height':30,
        'x_cord':150,
        'y_cord':20
    }




    AOM.append(config)
    AOM.append(testportal)
    AOM.append(testportal1)
    AOM.append(testportal2)
    AOM.append(testportal3)
    AOM.append(testportal4)
    AOM.append(testportal5)






    return AOM

def getTestContextMap():


    ContexMap={
        'config':{'flag':'ground'},
        '1':{'sig':'no','x': '400', 'y': '900', 'edges':['2']},
        '2':{'sig':'no','x': '400', 'y': '650', 'edges':['1','2','5','3']},
        '3':{'sig':'no','x': '400', 'y': '560', 'edges':['2','8','4']},
        '4':{'sig':'no','x': '400', 'y': '280', 'edges':['3','7']},
        '5':{'sig':'no','x': '220', 'y': '650', 'edges':['2','6']},
        '6':{'sig':'no','x': '220', 'y': '800', 'edges':['5']},
        '7':{'sig':'no','x': '200', 'y': '280', 'edges':['4']},
        '8':{'sig':'no','x': '700', 'y': '560', 'edges':['3','9']},
        '9':{'sig':'no','x': '700', 'y': '700', 'edges':['8']}

    }


#key 'nodename' sig:'no'
    return ContexMap



def get_image_srcs():


    srcs={
        'RS':{'1':"../static/image/rsGround.svg",
              '2':"../static/image/rs2.svg",
              '3':"../static/image/rs3.svg",
              '4':"../static/image/rs4.svg"

              }


    }

    return srcs