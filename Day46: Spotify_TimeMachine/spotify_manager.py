import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotify_client_id = os.environ['SPOTIFY_CLIENT_ID']
spotify_secret = os.environ['SPOTIFY_SECRET']
usern = os.environ['SPOTIFY_USER_ID']
redirect_url = "http://example.com"


class SpotifyManager:

    def __init__(self):
        self.song_list = None
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth
            (
                    client_id=spotify_client_id,
                    client_secret=spotify_secret,
                    redirect_uri=redirect_url,
                    scope="playlist-modify-private",
                    username=usern
                )
        )
        self.spotify_uri_list = []

    def get_uri_list(self, song_list):

        self.song_list = song_list
        for song in song_list:
            results = self.sp.search(q=f"track: {song}", limit=1)
            try:
                song_uri = results['tracks']['items'][0]['uri']
                self.spotify_uri_list.append(song_uri)
            except IndexError:
                pass

        return self.spotify_uri_list

    def load_playlist(self, date):

        playlist_id_ = self.sp.user_playlist_create(
            user=usern,
            name=f"{date} Billboard 100",
            public=False,
            description="a playlist made by a snake"
        )['id']
        self.sp.user_playlist_add_tracks(
            user=usern,
            playlist_id=playlist_id_,
            tracks=self.spotify_uri_list,
            position=None)
