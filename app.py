from flask import Flask, request, render_template, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import yaml

uri = "mongodb+srv://scarlett:<password>@cluster1.gmttnh0.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
mydb = client["hackathon_2023"]
mycol1 = mydb["querystats_transformed"]
mycol2 = mydb["out_querystats"]
mycol3 = mydb["querystats_combined"]
mycol4 = mydb["centroid"]

app = Flask(__name__)
def get_query_result_col1(text1):
   # text1 = text1.upper()
   # text2 = text2.upper()
   # combine = text1 + text2
   query_result = str(mycol1.find_one({'_id': {'oid': <org_id>}}))
   # '651192e13b4ae784aea798f9'
   return query_result

def combine_text(text2,text3):
    if text2 != 'CrudActorAggregate':
        return 'yaml type still in development'

    text3 = text3.upper()
    with open('/Users/scarlett/PycharmProjects/hackathon_2023/CrudActorAggregate.yml') as file:
        yaml_file = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    for i in yaml_file['Actors'][0]['Phases'][0]['Operations']:
        i['OperationCommand']['Pipeline'][0]['$match']['x'] = text3

    # combine = text2 + text3
    return str(yaml_file)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/query', methods=['GET','POST'])
def my_form_post_text2():
    text2 = request.form['text2']
    query_result = get_query_result_col1(text2)
    result = {
        "output": query_result
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
@app.route('/print', methods=['GET','POST'])
def combine_text_print():
    text2 = request.form['text2']
    text3 = request.form['text3']
    string = combine_text(text2, text3)
    result = {
        "output": string
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
