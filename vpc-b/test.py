from flask import Flask, abort, request, jsonify

app = Flask(__name__)

@app.route('/v2/color', methods=['GET'])
def get_color():
  try:
    color_name = request.args['name']
    color_hash = request.args['hash']

    ret = {'code': '', 'name': '', 'version': 'v2'}

    if color_name == 'red':
        ret['code'] = 'ffff00'
        ret['name'] = 'yellow'
    elif color_name == 'blue':
        ret['code'] = '800080'
        ret['name'] = 'purple'
    else:
        ret['code'] = '000000'
        ret['name'] = 'dark'

    return jsonify(ret), 200
  except Exception as e:
    print(e)
    abort(500)

@app.route('/v2/health', methods=['GET'])
def get_health():
  try:
    ret = {
        'version': 'v2',
        'status': 'ok'
    }

    return jsonify(ret), 200
  except Exception as e:
    print(e)
    abort(500)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8081)
