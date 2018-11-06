from flask import Flask, request, jsonify, send_from_directory, abort,app
import os
from flask import make_response

app = Flask(__name__)




@app.route("/download/<filepath>", methods=['GET'])
def download_file(filepath):
    # 此处的filepath是文件的路径，但是文件必须存储在static文件夹下， 比如images\test.jpg
    return app.send_static_file(filepath)


if __name__ == '__main__':
    app.run()