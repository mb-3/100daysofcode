from spotify_manager import SpotifyManager
from bb_data_manager import BBDataManager

selected_date = input("Please select a date to travel back to (YYYY-MM-DD): ")

bb = BBDataManager()
sm = SpotifyManager()

bb_data = bb.get_data(selected_date)
uri_list = sm.get_uri_list(bb_data)
sm.load_playlist(selected_date)



