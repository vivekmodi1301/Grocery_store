from flask import Flask , request , jsonify
import products_dao

from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()
@app.route("/get_products", methods = ['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__ == "__main__":
    print("start python Flask server for Grocery store management system")
    app.run(port=5000)