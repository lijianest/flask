from flask import Flask
from flask_restful import Resource
from flask_restful import Api
from flask_restful import request
app = Flask(__name__)
api = Api(app)

class Todo1(Resource):
    def get(self):
        return {'task':'helloword'}

class Todo2(Resource):
    def get(self):
        return {'task':'helloword'},201

class Todo3(Resource):
    def get(self):
        return {'task':'helloword'},201,{'Etag':'some'}

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


todos = {'todo2':'ok'}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

#api.add_resource(TodoSimple, '/<string:todo_id>')
#api.add_resource(HelloWorld, '/')
api.add_resource(HelloWorld, '/','/hello')
api.add_resource(TodoSimple,'/<string:todo_id>/todo_ep',endpoint = 'todo_ep')





if __name__ == '__main__':
    app.run(debug=True)
