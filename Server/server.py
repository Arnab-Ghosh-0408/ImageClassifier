from flask import Flask,request,jsonify
import Server_util




app=Flask(__name__)

@app.route("/classify_image",methods=['GET','POST'])
def classify_image():
    image_data = request.form['image_data']
    
    response = jsonify(Server_util.classify_image(image_data))
    
    response.headers.add("Access-Control-Allow-Origin",'*')
    
    return response

if __name__ == "__main__":
    print("Starting Flask Server for Sports Celebrity Image Classifier")
    Server_util.load_saved_artifacts()
    app.run(port=5000)