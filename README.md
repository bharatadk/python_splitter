# `Python Splitter` [![Downloads](https://static.pepy.tech/personalized-badge/python-splitter?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/python-splitter)

<div align="center">
  <br>
  <img alt="Open Sauced" src="https://i.ibb.co/7jPXt0Z/logo1-92f1a87f.png" width="300px">
  <h1>🍕 Open Sauced 🍕</h1>
  <strong>The path to your next Open Source contribution</strong>
</div>
<br>

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
$ python_splitter.split_from_folder("SOURCE_FOLDER", train = 0.5, test = 0.5)
But, this will not create "val" folder because train+test=0.5+0.5 =1.0
# SOURCE_FOLDER = PATH_TO_THE_FOLDER_CONTAINING_IMAGE_CLASSES_FOLDERS
```
![image](https://user-images.githubusercontent.com/51126350/201512419-305e313a-6e15-4c8c-892e-e34dec3f732e.png)

The splitted folder (train, test, and val) will be inside "Train_Test_Folder/" 

```python
import os

$ python_splitter.split_from_folder("SOURCE_FOLDER", train = 0.5, test = 0.3, val = 0.2)

$ print(os.listdir('Train_Test_Folder/')) # ['train', 'test', 'val']
```

To Access splitted folder (train, test, and val)

```python
import os

$ print(os.listdir('Train_Test_Folder/train/')) # ['cat', 'dog', 'pig']
$ print(os.listdir('Train_Test_Folder/test/')) # ['cat', 'dog', 'pig']
$ print(os.listdir('Train_Test_Folder/val/')) # ['cat', 'dog', 'pig']
```

## Starred By
<img src='https://avatars.githubusercontent.com/u/94124578?v=4' width='25' height='25'>	<img src='https://avatars.githubusercontent.com/u/51126350?v=4' width='25' height='25'>	<img src='https://avatars.githubusercontent.com/u/27841491?v=4' width='25' height='25'>	<img src='https://avatars.githubusercontent.com/u/97297013?v=4' width='25' height='25'>	<img src='https://avatars.githubusercontent.com/u/84966248?v=4' width='25' height='25'>	