from flask import Flask
from flask_restful import Resource, Api, reqparse
import scraper
import json

app = Flask(__name__)
api = Api(app)

# Define parser and request args
parser = reqparse.RequestParser()
parser.add_argument('date', type=str, required=False)
parser.add_argument('currency', type=str)
parser.add_argument('start_date', type=str, required=False)
parser.add_argument('end_date', type=str, required=False)

class Currency(Resource):
    def get(self):
        args = parser.parse_args()
        args = {k:v for k,v in args.items() if v is not None}
        if len(args) == 2:
            date = args['date']
            currency = args['currency']
            values = scraper.single_date(date, currency)
            return {
                "date": values[0],
                "currency": values[1],
                "Rate": values[2]
            }
        
        elif len(args) == 3:
            start_date = str(args['start_date'])
            end_date = str(args['end_date'])
            currency = str(args['currency'])
            values = scraper.range_dates(start_date, end_date, currency)
            return {
                "start_date": values[0],
                "end_date": values[1],
                "currency": values[2],
                "mean": values[3],
                "max": values[4],
                "min": values[5]
            }

api.add_resource(Currency, '/items')
app.run(host='0.0.0.0', port=5000)
