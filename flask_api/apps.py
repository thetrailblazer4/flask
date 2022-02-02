from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Emp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    desg = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"{self.name} - {self.desg}"



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/emps")
def get_emps():
    emps = Emp.query.all()

    output = []
    for i in emps:
        emp_data = {'name': i.name, 'desg':i.desg}
        output.append(emp_data)

    return {"emps":output}

@app.route("/emps/<id>")
def get_emp(id):
    emp = Emp.query.get_or_404(id)

    return {'name':emp.name, 'desg':emp.desg}

@app.route("/emps", methods=['POST'])
def add_emp():
    emp = Emp(name=request.json['name'], 
             desg=request.json['desg'])
    db.session.add(emp)
    db.session.commit()
    return {'id':emp.id}



