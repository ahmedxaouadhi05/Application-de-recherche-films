import tkinter as tk
from tkinter import messagebox
import requests

# OMDB API key (replace with your own key)
API_KEY = "9b535a30"
API_URL = "http://www.omdbapi.com/?i=tt3896198&apikey=9b535a30"

# Function to fetch movie details from OMDB API
def search_movie():
    movie_title = movie_entry.get()
    
    if not movie_title:
        messagebox.showwarning("Input Error", "Please enter a movie title.")
        return

    try:
        # Send request to OMDB API
        params = {"t": movie_title, "apikey": API_KEY}
        response = requests.get(API_URL, params=params)
        data = response.json()

        if data["Response"] == "True":
            # Movie found, display details
            title_label.config(text=f"Title: {data['Title']}")
            year_label.config(text=f"Year: {data['Year']}")
            director_label.config(text=f"Director: {data['Director']}")
            plot_label.config(text=f"Plot: {data['Plot']}")
        else:
            # Movie not found
            messagebox.showerror("Error", f"Movie not found: {movie_title}")
            clear_movie_details()

    except requests.exceptions.RequestException as e:
        # Handle connection errors
        messagebox.showerror("Error", f"Failed to fetch data: {e}")
        clear_movie_details()

# Function to clear the movie details from the labels
def clear_movie_details():
    title_label.config(text="Title: N/A")
    year_label.config(text="Year: N/A")
    director_label.config(text="Director: N/A")
    plot_label.config(text="Plot: N/A")

# Create the main window
root = tk.Tk()
root.title("Movie Search - OMDB API")

# Title label
app_title = tk.Label(root, text="Movie Search", font=("Arial", 18))
app_title.pack(pady=20)

# Input field to enter movie title
movie_entry = tk.Entry(root, font=("Arial", 12), width=40)
movie_entry.pack(pady=10)

# Button to search for the movie
search_button = tk.Button(root, text="Search Movie", font=("Arial", 12), command=search_movie)
search_button.pack(pady=10)

# Labels to display movie details
title_label = tk.Label(root, text="Title: N/A", font=("Arial", 12), wraplength=400)
title_label.pack(pady=5)

year_label = tk.Label(root, text="Year: N/A", font=("Arial", 12), wraplength=400)
year_label.pack(pady=5)

director_label = tk.Label(root, text="Director: N/A", font=("Arial", 12), wraplength=400)
director_label.pack(pady=5)

plot_label = tk.Label(root, text="Plot: N/A", font=("Arial", 12), wraplength=400)
plot_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
