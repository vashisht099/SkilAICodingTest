from flask import Flask, request, jsonify
import pandas as pd
app = Flask(__name__)

data = [
    {
        'city': 'New York',
        'gender': 'Male',
        'population': 4125000
    },
{
        'city': 'Chicago',
        'gender': 'Female',
        'population': 1400000
}
]

@app.route("/city_population/<string>:city_name", methods = ['GET'])
def get_names(city_name):
    for city in data:
        if city['city'] == city_name:
            return jsonify({city})
    return jsonify({'message': 'Item not found'})


if __name__ == "__main__":
    app.run(debug = True)
