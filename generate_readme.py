import requests

# Set the repository owner and name
owner = "bharatadk"
repo = "python_splitter"

# Get the list of users who have starred the repository using the GitHub API
response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/stargazers")
stargazers = response.json()

# Extract the avatar URLs for each stargazer
avatars = [stargazer["avatar_url"] for stargazer in stargazers]

# Get the current content of the README.md file
with open("README.md", "r") as file:
    content = file.read()

# Delete the existing stargazers list from the README.md file
if "## Starred By" in content:
    content = content.split("## Starred By")[0]

# Append the list of stargazers and their images to the end of the README.md file
content += "## Starred By\n"
for i, stargazer in enumerate(stargazers):
    content += f"<img src='{avatars[i]}' width='25' height='25'>\t"
content += "\n 👏👏👏"

# Write the updated content to the README.md file
with open("README.md", "w") as file:
    file.write(content)
