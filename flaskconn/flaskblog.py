from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from datetime import datetime,timedelta
from dateutil import tz


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20),nullable=True)
    cases_failed=db.Column(db.Integer,nullable=True)
    cases_passed=db.Column(db.Integer,nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow())


    def __init__(self,name,cases_failed,cases_passed):
        self.name=name
        self.cases_failed=cases_failed
        self.cases_passed=cases_passed


@app.route('/')
def listallusers():
    now = datetime.now()
    eight_hours_ago = now - timedelta(minutes=1)
    recent = datetime.now(tz=tz.tzlocal()) - timedelta(hours=6)

    person=User.query.filter(User.date >= recent).order_by(User.date).all()
    #person=User.query.all()[::-1]
    return render_template('list_all_users.html',mypersons=person)


if __name__=='__main__':
    app.run(debug=True)
