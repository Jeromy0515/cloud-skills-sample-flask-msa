from flask import Flask, abort, request, jsonify
import requests
# Modify url to Internal ALB DNS name
url = 'http://localhost:8081'
app = Flask(__name__)

@app.route('/v1/color', methods=['GET'])
def get_color():
  try:
    color_name = request.args['name']
    color_hash = request.args['hash']
    params = {'name': color_name, 'hash': color_hash}

    res = requests.get(url + '/v1/color', params)

    ret = {'code': res.json()['code'], 'name': res.json()['name']}

    return jsonify(ret), 200
  except Exception as e:
    print(e)
    abort(500)

@app.route('/health', methods=['GET'])
def get_health():
  try:
    res = requests.get(url + '/health')
    ret = {
        'status_code': str(res.status_code),
        'status': res.json()['status']
    }

    return jsonify(ret), 200
  except Exception as e:
    abort(500)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
