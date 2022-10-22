from os import environ
from supabase import create_client, Client
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)


TABLE = "data"

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

parser = reqparse.RequestParser()
# parser.add_argument('task')

# def update_data(data, id):
#     supabase.table(TABLE).update(data).eq("id", id).execute()
#     print('Updated Successfully')


# def delete_data(id):
#     supabase.table(TABLE).delete().eq('id', id).execute()
#     print('Deleted Successfully')


# def insert_data(data):
#     supabase.table(TABLE).insert(data).execute()
#     print('Inserted Successfully')


# def get_data():
#     data = []
#     print(data)


class home(Resource):
    def get(self):
        return "Nikhil Kumar"

class update(Resource):
    def get(self):
        status = request.args.get('status', type=str)
        device_id = request.args.get('id', type=int)
        # Below is the JSON Parser
        # parser = reqparse.RequestParser()
        # parser.add_argument('status', type = string, help = 'Device Status Update')
        # status = parser.parse_args(strict=True)
        response = supabase.table(TABLE).update({'status' : status}).eq("device_id", device_id).execute()
        # print(status)
        # return jsonify(status)
        return {'status' : response.data}, 200


class log(Resource):
    def get(self):
        response = supabase.table(TABLE).select('*').execute()
        # print(data.data)
        return jsonify(response.data)

class insert(Resource):
    def get(self):
        parser.add_argument('status', type = str)
        parser.add_argument('latitude', type = float)
        parser.add_argument('longitude',  type = float)
        parser.add_argument('device_id', type = int)
        data = parser.parse_args(strict= True)
        supabase.table(TABLE).insert(data).execute()
        print(data)
        return {'Device' : data} , 201

class delete(Resource):
    def get(self):
        device_id = request.args.get('id')
        supabase.table(TABLE).delete().eq('device_id', device_id).execute()
        return {'Deleted' : device_id}, 200

# insert_data({'name' : 'Hagesh'})
# update_data({'status' : 'false'}, 11)

# delete_data(12)


api.add_resource(log, '/log')
api.add_resource(update, '/update')
api.add_resource(insert,'/insert')  
api.add_resource(delete,'/delete')  
api.add_resource(home,'/')  

if __name__ == '__main__':
    app.run(debug=True, port=environ.get("PORT", 5000))
