from flask import Flask, render_template, request, redirect, session
from sqlalchemy import create_engine
from wtforms import Form, BooleanField, StringField, validators, SubmitField


from app.helper import gettestAOM
import app.helper as helper
import app.search as search
import app.mapTools as mT
import app.master as master

app = Flask(__name__)


class BuildingForm(Form):
    BuildingName = StringField('From', [validators.Length(min=0, max=25)])
    From = StringField('From', [validators.Length(min=0, max=25)])
    To = StringField('To', [validators.Length(min=0, max=35)])


class CampusForm(Form):
    From = StringField('From', [validators.Length(min=0, max=25)])
    To = StringField('To', [validators.Length(min=0, max=35)])


class ScheduleForm(Form):
    From = StringField('From', [validators.Length(min=0, max=25)])
    To = StringField('To', [validators.Length(min=0, max=35)])


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/Navigation-In-Campus/', methods=['POST'])
def campus():
    return render_template('cindex.html')


@app.route('/Navigation-In-Building/', methods=['POST'])
def building():
    form = BuildingForm(request.form)


    if request.method == 'POST' and form.validate():
        From='null'
        BuildingName='null'
        To='null'

        BuildingName = form.BuildingName.data
        From = form.From.data
        To = form.To.data
        if isinstance(To, str) and (To=='')==False:
            if isinstance(From, str)and (From=='')==False:
                AOM = master.the_magic_machine(From, To)
                return render_template('bindex.html', form=form, AOM=AOM)
            else:
                AOM = master.the_magic_machine('RS Main Entrance', To)
                return render_template('bindex.html', form=form, AOM=AOM)

        #return render_template('test.html', b=BuildingName, f=From, t=To, AOM=AOM)

        AOM = master.the_magic_machine('RS Main Entrance', 'RS Ground Pathpoint 1')
        return render_template('bindex.html', form=form, AOM=AOM)


@app.route('/scheduling/', methods=['POST'])
def schedule():
    return render_template('sindex.html')


@app.route('/news/', methods=['POST'])
def news():
    return render_template('nindex.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
