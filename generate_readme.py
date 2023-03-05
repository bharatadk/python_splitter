import requests

# Set the repository owner and name
owner = "bharatadk"
repo = "python_splitter"

# Get the list of users who have starred the repository using the GitHub API
response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/stargazers")
stargazers = response.json()

# Extract the avatar URLs and profile URLs for each stargazer
avatars = [stargazer["avatar_url"] for stargazer in stargazers]
profiles = [stargazer["html_url"] for stargazer in stargazers]

# Generate the resized and rounded avatar images using Pillow
size = 25
rounded_avatars = []
for avatar in avatars:
    response = requests.get(avatar)
    image = Image.open(BytesIO(response.content))
    image = image.resize((size, size))
    bigsize = (image.size[0] * 3, image.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(image.size, Image.ANTIALIAS)
    image.putalpha(mask)
    rounded_avatar = BytesIO()
    image.save(rounded_avatar, format='png')
    rounded_avatars.append(rounded_avatar.getvalue())

# Get the current content of the README.md file
with open("README.md", "r") as file:
    content = file.read()

# Delete the existing stargazers list from the README.md file
if "## Starred By" in content:
    content = content.split("## Starred By")[0]

# Append the list of stargazers and their images to the end of the README.md file
content += "## Starred By\n"
for i, stargazer in enumerate(stargazers):
    content += f"<img src='data:image/png;base64,{rounded_avatars[i].decode('utf-8')}' width='{size}' height='{size}' style='border-radius:50%'>\t"


# Write the updated content to the README.md file
with open("README.md", "w") as file:
    file.write(content)
