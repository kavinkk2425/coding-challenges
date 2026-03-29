from flask import Flask, request, jsonify

app = Flask(__name__)





# Home routeS
@app.route('/')
def home():
    return "API is working!"




# GET API
@app.route('/get-data', methods=['GET'])
def get_data():
    data = {
        "name": "Kavin",
        "role": "Developer"
    }
    return jsonify(data)



# POST API
@app.route('/send-data', methods=['POST'])
def receive_data():
    user_data = request.json
    return jsonify({
        "message": "Data received",
        "data": user_data
    })




# Run server
if __name__ == '__main__':
    app.run(debug=True)