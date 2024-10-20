from flask import Blueprint, json, request
from src.what import what
# Crea un Blueprint para las rutas
main = Blueprint('main', __name__)

@main.route('/what')
def routeWhat():
    ask = request.args.get('ask')
    key = request.args.get('key')
    
    missing = {}
    if not ask or ask.strip() == '':
        missing['ask'] = 'undefined'
    if not key or key.strip() == '':
        missing['key'] = 'undefined'
    
    if missing:
        return json.dumps(missing), 400
    
    return what(ask,key)