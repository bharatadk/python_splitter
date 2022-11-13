# python_splitter

Currently experimenting and planning! More Features will be added soon...

Developed by Bharat Adhikari (c) 2022

```
#Installation: pip install python_splitter

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
