from flask_restplus import Namespace, Resource

api = Namespace('fantasy', description= 'fantasy baseball bunch')

@api.route('/')
class Fantasy(Resource):
    def get(self):
        return {"fantasy": "baseball bunch"}
