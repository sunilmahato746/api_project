from flask import Flask,jsonify,request,json


app=Flask(__name__)

courses=[{'course_id':10,
         'course_name':'python',
         'price':'3200 INR'
          },
{'course_id':20,
         'course_name':'java',
         'price':'3000 INR'
          },
{'course_id':30,
         'course_name':'ruby',
         'price':'3900 INR'
          }
         ]


@app.route("/")
def index():
    return "Welcome"

@app.route('/course/<int:id>/',methods=['GET'])
def get_course(id):
    elem=[elem for elem in courses if elem['course_id']==id]
    return jsonify({'course':elem})

@app.route('/course/',methods=['POST'])
def create():
    payload=request.data
    print(payload)
    print(json.loads(payload))
    courses.append(json.loads(payload))
    return jsonify({})

@app.route('/course/<int:id>/',methods=['PUT'])
def update(id):
    payload=request.data
    print(payload)
    for elem in courses:
        if elem['course_id']==id:
            elem.update(json.loads(payload))
    return "record updated"

@app.route('/course/<int:id>/',methods=['DELETE'])
def delete(id):

    for elem in courses:
        if elem['course_id']==id:
            courses.remove(elem)
    return "record deleted"


if __name__=="__main__":
    app.run(debug=True)
