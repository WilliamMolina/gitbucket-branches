import json
import gitbucket
from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

## Resource class
class GitBucket(Resource):
    def get(self):
        return json.loads(gitbucket.obtener_ramas()), 200

##
## Actually setup the Api resource routing here
##
api.add_resource(GitBucket,'/branches')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")