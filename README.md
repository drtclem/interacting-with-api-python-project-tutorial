# Spotify API Analysis: The Strokes

An end-to-end data project using the Spotify API to pull, transform, and analyze track data for The Strokes — including a statistical look at whether song duration predicts popularity.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup & Configuration](#setup--configuration)
- [Analysis Workflow](#analysis-workflow)
- [Key Finding](#key-finding)
- [Tech Stack](#tech-stack)
- [Author](#author)

---

## Overview

This project connects to the Spotify API via the `Spotipy` Python library to retrieve album and track data for The Strokes. It then explores the relationship between song duration and popularity using scatter plots and linear regression.

---

## Project Structure



---

## Setup & Configuration

**1. Create a Spotify Developer account**

Go to the [Spotify Developer Dashboard](https://developer.spotify.com/documentation/web-api), log in, and create an application to get your `CLIENT_ID` and `CLIENT_SECRET`.

**2. Install dependencies**

```bash
pip install spotipy python-dotenv pandas numpy matplotlib scipy
```

**3. Configure environment variables**

Create a `.env` file in the project root:




---

## Analysis Workflow

**1. Connect to the Spotify API**
Authenticate using `SpotifyClientCredentials` and initialize the `Spotipy` client.

**2. Pull album and track data**
Retrieve the full album catalog and top 10 tracks for The Strokes using the artist URI.

**3. Transform the data**
- Build a Pandas DataFrame from the track dictionaries
- Convert `duration_ms` to a decimal minutes format
- Sort by popularity and surface the top 3 tracks

**4. Visualize and model**
- Scatter plot of duration vs. popularity with a linear regression line overlaid
- R-value reported to quantify the strength of the relationship
- Second plot with adjusted axes for a zoomed-out view

---

## Key Finding

There is a weak positive relationship between song duration and popularity for The Strokes' top tracks. Duration alone is not a meaningful predictor of how popular a song will be.

---

## Tech Stack

- Python
- Spotipy
- Pandas, NumPy
- Matplotlib
- SciPy (linregress)

---

## Author

Taylor Clements, PhD
