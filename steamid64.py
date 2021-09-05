import requests

class SteamApi():
    def __init__(self, apikey):
        self.apikey = apikey

    def getSteamId64(self, id):
        if isinstance(id, int) == True:
            return id
        
        else:
            custom_id = str(id).split("https://steamcommunity.com/id/")
            custom_id = "".join(custom_id)
            response = requests.get(f"http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={self.apikey}&vanityurl={custom_id}")
            return response.json()

steam = SteamApi(apikey="YOUR_STEAM_API_KEY")

print(steam.getSteamId64(id="jokerdes"))
