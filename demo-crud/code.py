from flask import Flask, request

app = Flask(__name__)


# http://127.0.0.1:5000/index?page=1&pageSize=20
@app.route('/index', methods=['GET'])
def index():
    # 获取页码，默认值为 1
    page = request.args.get('page', 1, type=int)
    # 获取每页数量，默认值为 20
    page_size = request.args.get('pageSize', 20, type=int)
    # 以字典形式返回数据，方便前端解析
    page1 = request.json.get('page1', 1, type=int)
    page_size1 = request.json.get('pageSize1', 20, type=int)
    return {
        "page": page,
        "pageSize": page_size,
        "page1": page1,
        "pageSize1": page_size1,
    }


@app.route("/submit", methods=['POST'])
def submit():
    page = request.form.get('page', 1, type=int)
    page_size = request.form.get('pageSize', 20, type=int)
    return {
        "message": "post请求的案例",
        "status": 200,
        "params": {
            "page": page,
            "pageSize": page_size
        }
    }


if __name__ == '__main__':
    app.run()
