from flask import Flask, request

app = Flask(__name__)

@app.route('/index')
def index():
    # 获取页码，默认值为 1
    page = request.args.get('page', 1, type=int)
    # 获取每页数量，默认值为 20
    page_size = request.args.get('pageSize', 20, type=int)
    # 以字典形式返回数据，方便前端解析
    return {
        "page": page,
        "pageSize": page_size
    }

if __name__ == '__main__':
    app.run()