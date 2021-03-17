from flask import Flask,jsonify,request,json



app=Flask(__name__)


@app.route("/")
def index():
    with open('data.json', 'r+') as f:
        return json.loads(f.read())


@app.route('/<int:id>/',methods=['GET'])
def get_course(id):

    with open('data.json','r+') as f:
        courses=json.loads(f.read())
        for k,v in courses.items():
            if courses[k]['course_id']==id:
                elem=courses[k]
                return elem


@app.route('/',  methods=['POST'])
def create():
    payload=request.data
    print(payload)
    print(json.loads(payload))
    with open('data.json', 'r+') as f:
        courses=json.loads(f.read())
        courses.update(json.loads(payload))
        f.truncate(0)
        f.seek(0)
        f.write(json.dumps(courses))
        return "courses"




@app.route('/<int:id>/',methods=['PUT'])
def update(id):
    payload=request.data
    print(payload)
    with open('data.json','r+') as f:
        courses=json.loads(f.read())

        courses[str(id)].update(json.loads(payload))
        f.truncate(0)
        f.seek(0)
        f.write(json.dumps(courses))
    return 'updated'




    return "record updated"



@app.route('/<int:id>/',methods=['DELETE'])
def delete_course(id):

    with open("data.json", "r+") as f:
        courses=json.loads(f.read())
        for k,v in courses.items():
            if courses[k]['course_id']==id:
                del courses[k]
                f.truncate(0)
                f.seek(0)
                f.write(json.dumps(courses))
                return "deleted"



if __name__=="__main__":
    app.run(debug=True)
