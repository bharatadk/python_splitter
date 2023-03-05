import requests

# Set the repository owner and name
owner = "bharatadk"
repo = "python_splitter"

# Get the list of users who have starred the repository using the GitHub API
response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/stargazers")
stargazers = response.json()

# Extract the avatar URLs for each stargazer
avatars = [stargazer["avatar_url"] for stargazer in stargazers]

# Generate the rounded avatar images using Avatarify
avatarify_url = "https://avatarify.ai/avatar"
avatarify_params = {"url": "", "size": 25, "round": True}
rounded_avatars = []
for avatar in avatars:
    avatarify_params["url"] = avatar
    response = requests.get(avatarify_url, params=avatarify_params)
    rounded_avatar = response.content.decode("utf-8")
    rounded_avatars.append(rounded_avatar)

# Get the current content of the README.md file
with open("README.md", "r") as file:
    content = file.read()

# Delete the existing stargazers list from the README.md file
if "## Starred By" in content:
    content = content.split("## Starred By")[0]

# Append the list of stargazers and their images to the end of the README.md file
content += "## Starred By\n"
for i, stargazer in enumerate(stargazers):
    content +=f"[![Image of {stargazer['login']}]({rounded_avatars[i]})]({profiles[i]})\n"


# Write the updated content to the README.md file
with open("README.md", "w") as file:
    file.write(content)
