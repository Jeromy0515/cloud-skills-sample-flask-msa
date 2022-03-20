from flask import Flask, abort, request, jsonify
import requests
# Modify url to Internal ALB DNS name
url = 'http://localhost:8081'
app = Flask(__name__)

@app.route('/<version>/color', methods=['GET'])
def get_color(version):
  try:
    color_name = request.args['name']
    color_hash = request.args['hash']
    params = {'name': color_name, 'hash': color_hash}

    res = requests.get(url + '/' + version + '/color', params)

    ret = {'code': res.json()['code'], 'name': res.json()['name'], 'version': res.json()['version']}

    return jsonify(ret), 200
  except Exception as e:
    print(e)
    abort(500)

@app.route('/<version>/health', methods=['GET'])
def get_health(version):
  try:
    res = requests.get(url + '/' + version + '/health')
    ret = {
        'version': res.json()['version'],
        'status_code': str(res.status_code),
        'status': res.json()['status']
    }

    return jsonify(ret), 200
  except Exception as e:
    print(e)
    abort(500)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
