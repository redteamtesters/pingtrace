import googlemaps
import requests

# Replace YOUR_API_KEY with your actual API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Get the IP address of the URL
url = input("Enter a URL: ")
ip = requests.get(f"https://api.hackertarget.com/hostsearch/?q={url}").text.split(",")

# Ping the IP address and get the hops
hops = requests.get(f"https://api.hackertarget.com/mtr/?q={ip}").text.split("\n")[1:-1]

# Create a list of locations from the hops
locations = []
for hop in hops:
    hop_parts = hop.split()
    if hop_parts[1] != "*":
        locations.append((float(hop_parts[2]), float(hop_parts[3])))

# Plot the locations on a map
fig = gmaps.figure()
markers = gmaps.marker_layer(locations)
fig.add_layer(markers)
if len(locations) > 1:
    polyline = gmaps.polyline(locations)
    fig.add_layer(polyline)
fig
