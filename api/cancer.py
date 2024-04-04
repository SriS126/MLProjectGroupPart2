## Python Cancer Sample API endpoint
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

# Import the CancerModel class from the model file
from model.cancers import CancerModel

cancer_api = Blueprint('cancer_api', __name__,
                   url_prefix='/api/cancer')

api = Api(cancer_api)
class CancerAPI:
    class _Predict(Resource):
        
        def post(self):
            """ Semantics: In HTTP, POST requests are used to send data to the server for processing.
            Sending passenger data to the server to get a prediction fits the semantics of a POST request.
            
            POST requests send data in the body of the request...
            1. which can handle much larger amounts of data and data types, than URL parameters
            2. using an HTTPS request, the data is encrypted, making it more secure
            3. a JSON formated body is easy to read and write between JavaScript and Python, great for Postman testing
            """     
            # Get the cell data from the request
            cell = request.get_json()

            # Get the singleton instance of the CancerModel
            cancerModel = CancerModel.get_instance()
            # Predict the survival probability of the cell
            response = cancerModel.predict(cell)

            # Return the response as JSON
            return jsonify(response)

    api.add_resource(_Predict, '/predict')