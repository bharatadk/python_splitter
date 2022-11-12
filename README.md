# python_splitter

Currently experimenting and planning! More Features will be added soon...

Developed by Bharat Adhikari (c) 2022

## Examples of How To Use (Buggy Alpha Version)

Creating Train-Test folders

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
