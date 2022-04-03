"""
SFU CMPT 756
Sample application---playlist service.
"""

# Standard library modules
import logging
import sys
import time

# Installed packages
from flask import Blueprint
from flask import Flask
from flask import request
from flask import Response

from prometheus_flask_exporter import PrometheusMetrics

import requests

import simplejson as json

# The application

app = Flask(__name__)

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Playlist process')

bp = Blueprint('app', __name__)

db = {
    "name": "http://cmpt756db:30002/api/v1/datastore",
    "endpoint": [
        "read",
        "write",
        "delete",
        "update"
    ]
}


@bp.route('/', methods=['GET'])
@metrics.do_not_track()
def hello_world():
    return ("test: s3 is deployed successfully!")


@bp.route('/health')
@metrics.do_not_track()
def health():
    return Response("", status=200, mimetype="application/json")

@bp.route('/hello', methods=['GET'])
@metrics.do_not_track()
def hello():
    return ("hello")

@bp.route('/readiness')
@metrics.do_not_track()
def readiness():
    return Response("", status=200, mimetype="application/json")

@bp.route('/', methods=['POST'])
def create_playlist():
    """
    Create a playlist.
    """
    try:
        content = request.get_json()
        music_str = content['music_list']
        music_list = music_str.strip().split(",")
    except Exception:
        return json.dumps({"message": "error reading arguments"})
    url = db['name'] + '/' + db['endpoint'][1]
    response = requests.post(
        url,
        json={"objtype": "playlist",
              "music_list": music_list})
    return (response.json())

@bp.route('/<playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    """
    Get a playlist specified by playlist_id.
    """ 
    payload = {"objtype": "playlist", "objkey": playlist_id}
    url = db['name'] + '/' + db['endpoint'][0]
    response = requests.get(
        url,
        params=payload)
    
    return (response.json())

@bp.route('/<playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    """
    Delete a playlist specified by playlist_id.
    """    
    url = db['name'] + '/' + db['endpoint'][2]

    response = requests.delete(url,
                               params={"objtype": "playlist", "objkey": playlist_id})
    return (response.json())

@bp.route('/<playlist_id>/add/<new_music>', methods=['PUT'])
def add_music(playlist_id, new_music):
    """
    Add music to an existing playlist.
    """ 
    payload = {"objtype": "playlist", "objkey": playlist_id}
    url = db['name'] + '/' + db['endpoint'][0]
    playlist_response = requests.get(
        url,
        params=payload)

    playlist_json = playlist_response.json()

    if (playlist_json['Count'] == 0):
        return Response(json.dumps({"error": f"playlist {playlist_id} not found"}),
                status=401,
                mimetype='application/json')
    
    music_list = playlist_json["Items"][0]["music_list"]

    if new_music in music_list:
        return Response(json.dumps({"error": f"{new_music} already exist in the playlist"}),
                        status=401,
                        mimetype='application/json')

    music_list.append(new_music)
    url = db['name'] + '/' + db['endpoint'][3]
    response = requests.put(
        url,
        params={"objtype": "playlist", "objkey": playlist_id},
        json={"music_list": music_list})

    return (response.json())

@bp.route('/<playlist_id>/delete/<music>', methods=['PUT'])
def delete_music(playlist_id, music):
    """
    Delete music in an playlist.
    """ 
    payload = {"objtype": "playlist", "objkey": playlist_id}
    url = db['name'] + '/' + db['endpoint'][0]
    playlist_response = requests.get(
        url,
        params=payload)

    playlist_json = playlist_response.json()

    if (playlist_json['Count'] == 0):
        return Response(json.dumps({"error": f"playlist {playlist_id} not found"}),
                status=401,
                mimetype='application/json')
    
    music_list = playlist_json["Items"][0]["music_list"]

    if music not in music_list:
        return Response(json.dumps({"error": f"{music} is not in the playlist"}),
                        status=401,
                        mimetype='application/json')

    music_list.remove(music)
    url = db['name'] + '/' + db['endpoint'][3]
    response = requests.put(
        url,
        params={"objtype": "playlist", "objkey": playlist_id},
        json={"music_list": music_list})

    return (response.json())

@bp.route('/<playlist_id>/top/<music>', methods=['PUT'])
def top_music(playlist_id, music):
    """
    Set specific music to top of a playlist.
    """ 
    payload = {"objtype": "playlist", "objkey": playlist_id}
    url = db['name'] + '/' + db['endpoint'][0]
    playlist_response = requests.get(
        url,
        params=payload)

    playlist_json = playlist_response.json()

    if (playlist_json['Count'] == 0):
        return Response(json.dumps({"error": f"playlist {playlist_id} not found"}),
                status=401,
                mimetype='application/json')
    
    music_list = playlist_json["Items"][0]["music_list"]

    if music not in music_list:
        return Response(json.dumps({"error": f"{music} is not in the playlist"}),
                        status=401,
                        mimetype='application/json')

    music_list.insert(0, music_list.pop(music_list.index(music)))
    url = db['name'] + '/' + db['endpoint'][3]
    response = requests.put(
        url,
        params={"objtype": "playlist", "objkey": playlist_id},
        json={"music_list": music_list})

    return (response.json())

# All database calls will have this prefix.  Prometheus metric
# calls will not---they will have route '/metrics'.  This is
# the conventional organization.
app.register_blueprint(bp, url_prefix='/api/v1/playlist/')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        logging.error("Usage: app.py <service-port>")
        sys.exit(-1)

    p = int(sys.argv[1])
    # Do not set debug=True---that will disable the Prometheus metrics
    app.run(host='0.0.0.0', port=p, threaded=True)
