import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

with open('credentials.json') as f:
    credentials = json.loads(f.read())

print(credentials)
client_credentials_manager = SpotifyClientCredentials(client_id = credentials['client_id'], client_secret = credentials['client_secret'])
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

p_id = input('Enter playlist id: ')

track_response = sp.playlist_tracks(p_id)
tracks = track_response['items']

while track_response['next']:
    track_response = sp.next(track_response)
    tracks.extend(track_response['items'])

num_tracks = len(tracks)
print(f"Number of tracks: {num_tracks}")

metadata = []

for item in tracks:
    track = item['track']
    metadata.append(track['duration_ms'])

filename = input('Enter output filename: ')

with open(filename, 'w') as f:
    f.write(json.dumps(metadata))