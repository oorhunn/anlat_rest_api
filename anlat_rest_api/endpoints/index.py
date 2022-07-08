from flask_restful import Resource


# TODO add signup - login - be partner
class Index(Resource):
    def get(self):
        return 'Welcome to Index'
    def post(self):
        pass