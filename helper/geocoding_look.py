#%%

#%%
import requests

class geoLookup:
    def __init__(self):
        self.api_key = "YOUR_KEY_HERE"
        self.url = "https://maps.googleapis.com/maps/api/geocode/json?address="

    # Get the zip code from the address
    def getZipCode(self, address):
        address = address.replace(" ", "+")
        response = requests.get(self.url + address + "&key=" + self.api_key)
        data = response.json()
        postcode = None
        for result in data['results']:
            for component in result['address_components']:
                if 'postal_code' in component['types']:
                    postcode = component['long_name']
                    break
            if postcode:
                break
        return postcode

    # Get the zip code from the long and latitude
    def getZipCode_long_latitude(self, long, lat):
        response = requests.get(self.url + str(lat) + "," + str(long) + "&key=" + self.api_key)
        data = response.json()
        postcode = "not found"
        for result in data['results']:
            for component in result['address_components']:
                if 'postal_code' in component['types']:
                    postcode = component['long_name']
                    break
            if postcode:
                break
        return postcode
#%%
