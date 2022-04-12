"""
Python  API for the music service.
"""

# Standard library modules

# Installed packages
import requests
# import simplejson as json

class Playlist():
    """Python API for the music service.

    Handles the details of formatting HTTP requests and decoding
    the results.

    Parameters
    ----------
    url: string
        The URL for accessing the playlist service. Often
        'http://cmpt756s3:30003/'. Note the trailing slash.
    auth: string
        Authorization code to pass to the music service. For many
        implementations, the code is required but its content is
        ignored.
    """
    def __init__(self, url, auth):
        self._url = url
        self._auth = auth

    def create_playlist(self, content=None):
        """
        Create a playlist.
        """
        # music_list = []
        # if content is not None:
        #     music_str = content['music_list']
        #     music_list = music_str.strip().split(",")
        # payload = {"objtype": "playlist", "music_list": music_list}
        if content is not None:
            payload = {"objtype": "playlist", "music_list": content}
        else:
            payload = {"objtype": "playlist", "music_list": ''}
        # print(payload)
        # print(self._url)
        response = requests.post(
            self._url,
            json=payload
        )
        # print(self._url)
        # print(response)

        return (response.json())
        # return response.json()["playlist_id"]

    def get_playlist(self, playlist_id):
        """
        Get a playlist specified by playlist_id.
        """ 
        response = requests.get(
            self._url + playlist_id)
        # print("Response: ", response.json())
        
        return (response.json())

    def delete_playlist(self, playlist_id):
        """
        Delete a playlist specified by playlist_id.
        """    
        response = requests.delete(
            self._url + playlist_id)
        return (response.json())

    def add_music(self, playlist_id, new_music):
        """
        Add music to an existing playlist.
        """ 
        # playlist_response = requests.get(
        #     self._url + playlist_id)

        # playlist_json = playlist_response.json()
        
        # music_list = playlist_json["Items"][0]["music_list"]

        # music_list.append(new_music)

        response = requests.put(
            self._url + playlist_id + '/add/' + new_music
        )

        return (response.json())

    def delete_music(self, playlist_id, music):
        """
        Delete music in an playlist.
        """ 
        # payload = {"objtype": "playlist", "objkey": playlist_id}
        # playlist_response = requests.get(
        #     self._url,
        #     params=payload)

        # playlist_json = playlist_response.json()

        # if (playlist_json['Count'] == 0):
        #     print(json.dumps({"error": f"playlist {playlist_id} not found"}))
        #     return None    
        
        # music_list = playlist_json["Items"][0]["music_list"]

        # if music not in music_list:
        #     print(json.dumps({"error": f"{music} is not in the playlist"}))
        #     return None

        # music_list.remove(music)
        response = requests.put(
            self._url + playlist_id + '/delete/' + music
        )

        return (response.json())

    def top_music(self, playlist_id, music):
        """
        Set specific music to top of a playlist.
        """ 
        # payload = {"objtype": "playlist", "objkey": playlist_id}
        # playlist_response = requests.get(
        #     self._url,
        #     params=payload)

        # playlist_json = playlist_response.json()

        # if (playlist_json['Count'] == 0):
        #     print(json.dumps({"error": f"playlist {playlist_id} not found"}))
        #     return None
        
        # music_list = playlist_json["Items"][0]["music_list"]

        # if music not in music_list:
        #     print(json.dumps({"error": f"{music} is not in the playlist"}))
        #     return None

        # music_list.insert(0, music_list.pop(music_list.index(music)))
        # response = requests.put(
        #     self._url,
        #     params={"objtype": "playlist", "objkey": playlist_id},
        #     json={"music_list": music_list})

        response = requests.put(
            self._url + playlist_id + '/top/' + music
        )

        return (response.json())

