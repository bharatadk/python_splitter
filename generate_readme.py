import requests

# Set the repository owner and name
owner = "bharatadk"
repo = "python_splitter"

# Get the list of forks for the repository using the GitHub API
response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/forks")
forks = response.json()

# Extract the image URLs for each fork
images = [fork["owner"]["avatar_url"] for fork in forks]

# Format the list of forks and their images using Markdown syntax
content = "## Forks\n\n"
for i, fork in enumerate(forks):
    content += f"{i+1}. [{fork['full_name']}]({fork['html_url']})\n"
    content += f"   ![Image of {fork['owner']['login']}]({images[i]})\n"

# Write the formatted content to the README.md file
with open("README.md", "w") as file:
    file.write(content)
