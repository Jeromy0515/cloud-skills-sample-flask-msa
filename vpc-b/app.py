from flask import Flask, abort, request, jsonify

app = Flask(__name__)

@app.route('/v1/color', methods=['GET'])
def get_color():
  try:
    color_name = request.args['name']
    color_hash = request.args['hash']

    ret = {'code': '', 'name': '', 'version': 'v1'}

    if color_name == 'red':
        ret['code'] = 'f34a07'
        ret['name'] = 'orange'
    elif color_name == 'blue':
        ret['code'] = '71f0f9'
        ret['name'] = 'sky'
    else:
        ret['code'] = 'ff00ff'
        ret['name'] = 'pink'

    return jsonify(ret), 200
  except Exception as e:
    print(e)
    abort(500)

@app.route('/v1/health', methods=['GET'])
def get_health():
  try:
    ret = {
        'version': 'v1',
        'status': 'ok'
    }

    return jsonify(ret), 200
  except Exception as e:
    print(e)
    abort(500)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8081)
