import os
import pandas as pd
import numpy as np
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt
from scipy.stats import linregress



# Load the .env file variables
load_dotenv()

# Retrieve environment variables correctly
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
)

#This will find the albums for The Strokes
strokes_uri = 'spotify:artist:0epOFNiUfyON9EYx7Tpr6V'

results = spotify.artist_albums(strokes_uri, album_type='album')
albums = results['items']

while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])


for album in albums:
    print(album['name'])


#Now I want to get the top 10 songs from The Strokes

strokes_uri = 'spotify:artist:0epOFNiUfyON9EYx7Tpr6V'

top_tracks = spotify.artist_top_tracks(strokes_uri)
tracks = results['items']

print(f"{'No.':<4} {'Track Name':<40} {'Popularity':<10} {'Duration (min:sec)'}")
print("=" * 70)

track_data = []
for track in top_tracks['tracks']:
    track_data.append({
        'Track Name': track['name'],
        'Popularity (out of 100)': track['popularity'],
        'Duration (min:sec)': f"{track['duration_ms'] // 60000}:{(track['duration_ms'] % 60000) // 1000:02d}"
    })


df = pd.DataFrame(track_data)
print(df)

#This will fetch the top three songs by the strokes in terms of popularity
df_sorted =df.sort_values(by = 'Popularity (out of 100)', ascending=False)

print(df_sorted[:3])



print(df)

#Before analysis, I want to get the minutes into their full time in minutes

def convert_to_minute(time_str):
    minutes, sec = map(int, time_str.split(":"))
    return minutes + (sec/60)

df["Duration (min:sec)"] =df["Duration (min:sec)"].apply(convert_to_minute)
print(df[["Duration (min:sec)"]])

#Renaming the column with time to show how it's presented now
df.rename(columns={"Duration (min:sec)": "Duration (min)"}, inplace=True)
print(df)


#Going to analyze the data with Duration on the x-axis and Popularity on the y-axis. Then do a linear regression to see if the relationship is signifcant

plt.figure(figsize=(8,5))
plt.scatter(df["Duration (min)"], df["Popularity (out of 100)"], alpha=.7, label="Data", color="blue")

slope, intercept, r_value, p_value, std_err = linregress(df["Duration (min)"], df["Popularity (out of 100)"])
x_vals = np.linspace(df["Duration (min)"].min(), df["Duration (min)"].max(), 100)
y_vals = slope * x_vals + intercept

plt.plot(x_vals, y_vals, color='red', label=f"y = {slope:.2f}x + {intercept:.2f}\nR = {r_value:.2f}")


plt.xlabel("Duration (min)")
plt.ylabel("Popularity (out of 100)")
plt.title("Duration vs Popularity")
plt.legend()
plt.show()


# Print R-value
print(f"R-value: {r_value:.4f}")



plt.figure(figsize=(8,5))
plt.scatter(df["Duration (min)"], df["Popularity (out of 100)"], alpha=.7, label="Data", color="blue")

slope, intercept, r_value, p_value, std_err = linregress(df["Duration (min)"], df["Popularity (out of 100)"])
x_vals = np.linspace(df["Duration (min)"].min(), df["Duration (min)"].max(), 100)
y_vals = slope * x_vals + intercept

plt.plot(x_vals, y_vals, color='red', label=f"y = {slope:.2f}x + {intercept:.2f}\nR = {r_value:.2f}")


plt.xlabel("Duration (min)")
plt.ylabel("Popularity (out of 100)")
plt.title("Duration vs Popularity")
plt.xlim(0,6)
plt.ylim(0,100)
plt.legend()
plt.show()