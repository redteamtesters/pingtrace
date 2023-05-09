import tkinter as tk
from datetime import datetime
import googlemaps


# Create instance of Tkinter class
root = tk.Tk()
root.title("Google Maps GUI")

# Create entry widgets for inputting API key and address
api_key_label = tk.Label(root, text="Enter your Google Maps API Key:")
api_key_label.pack()
api_key_entry = tk.Entry(root)
api_key_entry.pack()
address_label = tk.Label(root, text="Enter an address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Create function for getting the latitude and longitude of an address
def get_lat_lng():
    # Get API key and address from entry widgets
    api_key = api_key_entry.get()
    address = address_entry.get()
    # Create instance of Google Maps API client
    gmaps = googlemaps.Client(api_key)
    # Get geocode result for address
    geocode_result = gmaps.geocode(address)
    # Extract latitude and longitude from geocode result
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    # Create label for displaying latitude and longitude
    lat_lng_label = tk.Label(root, text=f"Latitude: {lat}, Longitude: {lng}")
    lat_lng_label.pack()

# Create button for getting latitude and longitude
get_lat_lng_button = tk.Button(root, text="Get Latitude and Longitude", command=get_lat_lng)
get_lat_lng_button.pack()

root.mainloop()