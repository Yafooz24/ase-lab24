from flask import request,Flask,make_response,jsonify


app=Flask(__name__,instance_relative_config=True)


app.route("/lower")
def lower():
    a=request.args.get('a',0,type=str)
    if a :
        return make_response(jsonify(a.lower()),200)
    else:
        return make_response(jsonify("invalide inputs"),404)