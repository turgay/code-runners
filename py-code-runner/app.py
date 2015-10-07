from flask import Flask, jsonify, request

from flask import make_response

from code_runner import CodeRunner



app = Flask(__name__)


@app.route('/', methods=["GET"])
def back_test():
    return "This is not ment to be used by browser :)!"

@app.route('/pycoder/api/v1.0/run', methods=['POST'])
def run_code():
    if not 'code' in request.json:
        return jsonify({'error': 'Invalid code run call'}), 201

    code = request.json['code']

    print "code=", code

    try:
        err, out = CodeRunner().run(code)#CodeExecuter().execute(code)
        return jsonify({'result': True, 'error': err, 'output': out}), 201
    except Exception, ex:
        import traceback
        print traceback.format_exc()
        return jsonify({'result': False, 'error': ex}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, port=7000)