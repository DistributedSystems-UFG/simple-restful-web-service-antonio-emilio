#
# The original code for this example is credited to S. Subramanian,
# from this post on DZone: https://dzone.com/articles/restful-web-services-with-python-flask
#

from flask import Flask
from flask import jsonify
from flask import request
from flask import abort

app = Flask(__name__)

empDB=[
 {
 'id':'101',
 'name':'Saravanan S',
 'title':'Technical Leader',
 'salary': 1250
 },
 {
 'id':'201',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer',
 'salary': 1000
 }
 ]

@app.route('/empdb/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})

@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ] 
    
    if len(usr) == 0:
        return jsonify({'response':'Failure, no such employee'})
        
    return jsonify({'emp':usr})

# retrieve the average salary, considering all the employees;

@app.route('/empdb/employee/average',methods=['GET'])
def getAverageSalary():
    sum = 0
    for emp in empDB:
        sum += emp['salary']
        
    return jsonify({'average':sum/len(empDB)})


@app.route('/empdb/employee/<empId>',methods=['PUT'])
def updateEmp(empId):

    em = [ emp for emp in empDB if (emp['id'] == empId) ]

    if len(em) > 0:
        if 'name' in request.json : 
            em[0]['name'] = request.json['name']

        if 'title' in request.json:
            em[0]['title'] = request.json['title']

        if 'salary' in request.json:
            em[0]['salary'] = request.json['salary']

    return jsonify(em)


@app.route('/empdb/employee',methods=['POST'])
def createEmp():

    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'title':request.json['title'],
    'salary':request.json['salary']
    }
    empDB.append(dat)
    return jsonify(dat)

@app.route('/empdb/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]

    if len(em) > 0:
        empDB.remove(em[0])
        return jsonify({'response':'Success'})
    else:
        return jsonify({'response':'Failure'})

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
