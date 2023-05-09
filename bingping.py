import ping3
import googlemaps

# Set up API key for Google Maps
gmaps = googlemaps.Client(key='')

# Define the destination IP address
destination = '8.8.8.8'

# Get the ping hops
hops = ping3.trace(destination)

# Get the latitude and longitude for each hop
lat_lngs = []
for hop in hops:
    if hop[1] is not None:
        geocode_result = gmaps.geocode(hop[1])
        if geocode_result:
            location = geocode_result[0]['geometry']['location']
            lat_lngs.append((location['lat'], location['lng']))

# Plot the hops on a map
gmaps.new_static_map(size=(640, 640), path=lat_lngs)
