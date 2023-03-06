<div align="center">
  <br>
  <img alt="Open Sauced" src="https://i.ibb.co/7jPXt0Z/logo1-92f1a87f.png" width="300px">
  <h1>🍕 Open Sauced 🍕</h1>
  <strong>The path to your next Open Source contribution</strong>
</div>
<br>

# python_splitter

Currently experimenting and planning! More Features will be added soon...

Developed by Bharat Adhikari (c) 2022

```
#Installation:
pip install python_splitter
```

## Examples of How To Use 

Grouping Images into Classes
```python
import python_splitter
python_splitter.image_to_class('SOURCE_FOLDER')
```
![image](https://user-images.githubusercontent.com/51126350/201512011-056cdabf-de2f-4c00-b294-8fd31325ffe0.png)


Creating Train-Test folders (With Random-Shuffling Enabled)

```python
import python_splitter
$ python_splitter.split_from_folder("SOURCE_FOLDER", train = 0.5, test = 0.3, val = 0.2)
$ python_splitter.split_from_folder("SOURCE_FOLDER", train = 0.5, test = 0.3)
# Note: Both above code gives same result because 0.5+0.3=0.8 . 
	   So, val = 0.2 is calculated automatically.
$ python_splitter.split_from_folder("SOURCE_FOLDER, train = 0.5, test = 0.5)
But, this will not create "val" folder because train+test=0.5+0.5 =1.0
# SOURCE_FOLDER = PATH_TO_THE_FOLDER_CONTAINING_IMAGE_CLASSES_FOLDERS
```
![image](https://user-images.githubusercontent.com/51126350/201512419-305e313a-6e15-4c8c-892e-e34dec3f732e.png)

## Starred By
<img src='{'login': 'phuongnguyen194', 'id': 94124578, 'node_id': 'U_kgDOBZw6Ig', 'avatar_url': 'https://avatars.githubusercontent.com/u/94124578?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/phuongnguyen194', 'html_url': 'https://github.com/phuongnguyen194', 'followers_url': 'https://api.github.com/users/phuongnguyen194/followers', 'following_url': 'https://api.github.com/users/phuongnguyen194/following{/other_user}', 'gists_url': 'https://api.github.com/users/phuongnguyen194/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/phuongnguyen194/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/phuongnguyen194/subscriptions', 'organizations_url': 'https://api.github.com/users/phuongnguyen194/orgs', 'repos_url': 'https://api.github.com/users/phuongnguyen194/repos', 'events_url': 'https://api.github.com/users/phuongnguyen194/events{/privacy}', 'received_events_url': 'https://api.github.com/users/phuongnguyen194/received_events', 'type': 'User', 'site_admin': False}' width='25' height='25'>	<img src='{'login': 'bharatadk', 'id': 51126350, 'node_id': 'MDQ6VXNlcjUxMTI2MzUw', 'avatar_url': 'https://avatars.githubusercontent.com/u/51126350?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/bharatadk', 'html_url': 'https://github.com/bharatadk', 'followers_url': 'https://api.github.com/users/bharatadk/followers', 'following_url': 'https://api.github.com/users/bharatadk/following{/other_user}', 'gists_url': 'https://api.github.com/users/bharatadk/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/bharatadk/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/bharatadk/subscriptions', 'organizations_url': 'https://api.github.com/users/bharatadk/orgs', 'repos_url': 'https://api.github.com/users/bharatadk/repos', 'events_url': 'https://api.github.com/users/bharatadk/events{/privacy}', 'received_events_url': 'https://api.github.com/users/bharatadk/received_events', 'type': 'User', 'site_admin': False}' width='25' height='25'>	<img src='{'login': 'bertlandh', 'id': 27841491, 'node_id': 'MDQ6VXNlcjI3ODQxNDkx', 'avatar_url': 'https://avatars.githubusercontent.com/u/27841491?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/bertlandh', 'html_url': 'https://github.com/bertlandh', 'followers_url': 'https://api.github.com/users/bertlandh/followers', 'following_url': 'https://api.github.com/users/bertlandh/following{/other_user}', 'gists_url': 'https://api.github.com/users/bertlandh/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/bertlandh/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/bertlandh/subscriptions', 'organizations_url': 'https://api.github.com/users/bertlandh/orgs', 'repos_url': 'https://api.github.com/users/bertlandh/repos', 'events_url': 'https://api.github.com/users/bertlandh/events{/privacy}', 'received_events_url': 'https://api.github.com/users/bertlandh/received_events', 'type': 'User', 'site_admin': False}' width='25' height='25'>	<img src='{'login': 'bharatadhik', 'id': 97297013, 'node_id': 'U_kgDOBcyidQ', 'avatar_url': 'https://avatars.githubusercontent.com/u/97297013?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/bharatadhik', 'html_url': 'https://github.com/bharatadhik', 'followers_url': 'https://api.github.com/users/bharatadhik/followers', 'following_url': 'https://api.github.com/users/bharatadhik/following{/other_user}', 'gists_url': 'https://api.github.com/users/bharatadhik/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/bharatadhik/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/bharatadhik/subscriptions', 'organizations_url': 'https://api.github.com/users/bharatadhik/orgs', 'repos_url': 'https://api.github.com/users/bharatadhik/repos', 'events_url': 'https://api.github.com/users/bharatadhik/events{/privacy}', 'received_events_url': 'https://api.github.com/users/bharatadhik/received_events', 'type': 'User', 'site_admin': False}' width='25' height='25'>	<img src='{'login': 'Anuj-Gupta4', 'id': 84966248, 'node_id': 'MDQ6VXNlcjg0OTY2MjQ4', 'avatar_url': 'https://avatars.githubusercontent.com/u/84966248?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/Anuj-Gupta4', 'html_url': 'https://github.com/Anuj-Gupta4', 'followers_url': 'https://api.github.com/users/Anuj-Gupta4/followers', 'following_url': 'https://api.github.com/users/Anuj-Gupta4/following{/other_user}', 'gists_url': 'https://api.github.com/users/Anuj-Gupta4/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/Anuj-Gupta4/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/Anuj-Gupta4/subscriptions', 'organizations_url': 'https://api.github.com/users/Anuj-Gupta4/orgs', 'repos_url': 'https://api.github.com/users/Anuj-Gupta4/repos', 'events_url': 'https://api.github.com/users/Anuj-Gupta4/events{/privacy}', 'received_events_url': 'https://api.github.com/users/Anuj-Gupta4/received_events', 'type': 'User', 'site_admin': False}' width='25' height='25'>	