from flask import Flask, redirect, url_for, request
import SimilarImages
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3001", "http://localhost:5000"])

@app.route('/similarity', methods = ['POST'])
def similarity():
    if request.method == 'POST':
        u = request.get_json()
        print(u)
        similar_images_index_list = SimilarImages.find_similar(0,3,'goa_dataset')
        print(similar_images_index_list)
        return {'similar_images_index': similar_images_index_list}
 
# main driver function
if __name__ == '__main__':
    app.run(host='192.168.53.147' , port=5000)