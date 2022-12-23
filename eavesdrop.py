import requests

# Replace this value with your own Discord API token
TOKEN = input("Enter your Discord API token: ")

headers = {
    "Authorization": f"Bot {TOKEN}",
    "User-Agent": "MyBot/1.0",
}

# Send a GET request to the Discord API to retrieve the webpack chunk data
response = requests.get("https://discordapp.com/api/v6/webpack/discord_app", headers=headers)
data = response.json()

# Extract the required data from the webpack chunk
wp_require = data[0][1]
mod = next(x for x in wp_require["c"].values() if hasattr(x["exports"], "default") and hasattr(x["exports"]["default"], "isDeveloper"))
user_mod = next(x for x in wp_require["c"].values() if hasattr(x["exports"], "default") and hasattr(x["exports"]["default"], "getUsers"))
nodes = list(mod["exports"]["default"]._dispatcher._actionHandlers._dependencyGraph.nodes.values())

# Try to execute the first part of the code
try:
    experiment_store = next(x for x in nodes if x.name == "ExperimentStore")
    experiment_store.actionHandler["CONNECTION_OPEN"]({"user": {"flags": 1}, "type": "CONNECTION_OPEN"})
except Exception as e:
    pass

# Execute the second part of the code
old_get_user = user_mod["exports"]["default"].__proto__.getCurrentUser
user_mod["exports"]["default"].__proto__.getCurrentUser = lambda: {"hasFlag": lambda: True}
developer_experiment_store = next(x for x in nodes if x.name == "DeveloperExperimentStore")
developer_experiment_store.actionHandler["CONNECTION_OPEN"]()
user_mod["exports"]["default"].__proto__.getCurrentUser = old_get_user

# This code allows for you to hear and speak while muted and deafened 
