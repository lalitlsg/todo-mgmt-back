from flask_restful import Resource
from flask import make_response, request
import json
import http
from config import tasks
from bson import json_util, ObjectId

class Todo(Resource):
    def post(self):
        try:
            data = json.loads(request.data.decode("utf-8"))
            tasks.insert(data)
            return make_response(json.dumps({'message': 'Task Saved Successfully'}),
                                 http.HTTPStatus.OK)
        except Exception as e:
            return make_response(json.dumps({'message': str(e)}), http.HTTPStatus.BAD_REQUEST)

    def get(self):
        try:
            tasklist = []
            for i in tasks.find({}):
                tasklist.append(i)
            return make_response(json_util.dumps({'data': tasklist}),
                                 http.HTTPStatus.OK)
        except Exception as e:
            return make_response(json.dumps({'message': str(e)}), http.HTTPStatus.BAD_REQUEST)

    def put(self):
        try:
            data = json.loads(request.data.decode("utf"))
            id = data['id']
            tasks.update({'_id':ObjectId(id)},{
                '$set':{'status':'Completed'}
            })
            return make_response(json_util.dumps({'data': 'updated'}),
                                 http.HTTPStatus.OK)

        except Exception as e:
            return make_response(json.dumps({'message': str(e)}), http.HTTPStatus.BAD_REQUEST)

    def delete(self):
        try:
            data = json.loads(request.data.decode("utf"))
            id = data['id']
            tasks.delete_one({'_id':ObjectId(id)})
            return make_response(json_util.dumps({'data': 'deleted'}),
                                 http.HTTPStatus.OK)
        except Exception as e:
            return make_response(json.dumps({'message': str(e)}), http.HTTPStatus.BAD_REQUEST)