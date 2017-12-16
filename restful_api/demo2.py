from flask import Flask
from flask_restful import Resource
from flask_restful import Api
from flask_restful import request
app = Flask(__name__)
api = Api(app)
from flask_restful import reqparse
class GetValue(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('r'
                            ''
                            ''
                            'ate',type=int,action='append',help='Rate to charge for this resource',required=True,dest='num')
        parser.add_argument('xx',type=str,required=True,dest='xxx')
        args = parser.parse_args(strict=True)
        print args,args['num'], args['xxx']
        return args['num']
from collections import OrderedDict
from flask_restful import fields,marshal_with

resource_fileds = {'task':fields.String,
                   'url': fields.Url('todo_ep') }

class TodoDao(object):
    def __init__(self,todo_id,task):
        self.todo_id = todo_id
        self.task = task
        self.status = 'active'
class Todo(Resource):
    @marshal_with(resource_fileds)
    def get(self,**kwargs):
        return TodoDao(todo_id='myid',task='milk')

api.add_resource(GetValue,'/')
if __name__ == '__main__':
    app.run(debug=True)