from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello():
    print(request.get_data())
    return Response("test", status=200)


if __name__ == '__main__':
    app.run(debug=True, host='34.249.157.229', port=5000)



