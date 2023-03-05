import os
import glob
import numpy as np
import shutil
import re


class Train_test_split_class(object):
    def __init__(self):
        """
        Initializes an instance of the Train_test_split_class.
        """
        self.root_folder = ""
        self.new_root = "Train_Test_Folder"
        self.classes = []
        self.train_per = 0
        self.test_per = 0
        self.val_per = 0

    # class methods

    def generate_classes(self):
        """
        Generates class list from subfolders of root directory.

        Returns
        -------
        classes : list
            A list of class names extracted from the subfolders of the root directory.
        """
        self.classes = [
            name
            for name in os.listdir(self.root_folder)
            if os.path.isdir(os.path.join(self.root_folder, name))
            and name != "__pycache__"
        ]

    def path_validation(self):
        """
        Validates the paths of the root directory and the subdirectories.

        Raises
        ------
        ValueError
            If the root directory or subdirectories do not exist.
        """
        isExist = os.path.exists(self.root_folder)
        if isExist:

            return
        raise Exception("🐞The SOURCE PATH doesn't exits")

    def make_directories(self):
        """
        Creates directories for the train, test and validation sets.

        Raises
        ------
        OSError
            If the directories already exist or cannot be created.
        """
        if os.path.exists(self.new_root):
            shutil.rmtree(self.new_root)
        for cls in self.classes:
            os.makedirs(os.path.join(self.new_root, "train", cls))
            os.makedirs(os.path.join(self.new_root, "test", cls))

            if self.val_per > 0:
                os.makedirs(os.path.join(self.new_root, "val", cls))

        return

    def validation_per(self):
        """
        Calculates the percentage of validation set based on the train set.

        Returns
        -------
        None
        """
        print(self.train_per, self.val_per, self.test_per)

        if 0 < self.train_per < 1 and 0 < self.test_per < 1 and 0 <= self.val_per < 1:

            if (self.train_per + self.test_per) < 1.0 and self.val_per == 0:
                self.val_per = 1.0 - (self.train_per + self.test_per)

            if (self.train_per + self.test_per + self.val_per) == 1.0:
                return

            else:
                ex = "🐞The sum of train,test,split percentage is greater than 1 or 100%. \n Please adjust the train,test,val parameters again."
                raise Exception(ex)

        return

    def shuffle_and_copy_images(self):
        """
        Shuffles the images and copies them to the respective train, test and validation folders.

        """
        ## creating partition of the data after shuffeling
        for cls in self.classes:
            src = os.path.join(self.root_folder, cls)  # root_folder to copy images from

            allFileNames = os.listdir(src)

            np.random.shuffle(allFileNames)

            if self.val_per == 0:
                train_FileNames, test_FileNames = np.split(
                    np.array(allFileNames), [int(len(allFileNames) * self.train_per)]
                )
            else:
                train_FileNames, val_FileNames, test_FileNames = np.split(
                    np.array(allFileNames),
                    [
                        int(len(allFileNames) * self.train_per),
                        int(len(allFileNames) * (self.test_per + self.train_per)),
                    ],
                )

            ##Converting file names from array to list

            train_FileNames = [
                os.path.join(src, filename) for filename in train_FileNames
            ]

            if self.val_per != 0:
                val_FileNames = [
                    os.path.join(src, filename) for filename in val_FileNames
                ]
            test_FileNames = [
                os.path.join(src, filename) for filename in test_FileNames
            ]

            for file_name in train_FileNames:
                shutil.copy(file_name, os.path.join(self.new_root, "train", cls))

            if self.val_per != 0:

                for filename in val_FileNames:
                    shutil.copy(filename, os.path.join(self.new_root, "val", cls))

            for filename in test_FileNames:
                shutil.copy(filename, os.path.join(self.new_root, "test", cls))
        return


def split_from_folder(root_folder_path, train=0.8, test=None, val=None):
    """
    Parameters
    ----------
    root_folder_path : str
        The path to the root directory containing subdirectories with images.
    train : float, optional
        The percentage of images to be used for training (default is 0.8).
    test : float, optional
        The percentage of images to be used for testing (default is None).
    val : float, optional
        The percentage of images to be used for validation (default is None).

    Raises
    ------
    ValueError
        If the sum of train, test and validation percentages is not equal to 1.

    Notes
    -----
    At least one of test or val must be provided. If only test is provided, the remaining images will be used for validation.
    If both test and val are provided, they will be used as specified and train will be calculated accordingly.
    """
    try:
        obj = Train_test_split_class()
        obj.root_folder = root_folder_path
        obj.train_per = train
        if test is not None:
            obj.test_per = test
        if val is not None:
            obj.val_per = val

        obj.generate_classes()
        print("✅Checking SOURCE directory...")

        obj.validation_per()
        print("✅Checking percentage validation...")

        obj.make_directories()
        print("✅Making required directories...")

        obj.shuffle_and_copy_images()
        print("✅Shuffling data...")
        print("✅Getting ready for copying files...")

        print("\n-------------Successfully splitted !!!--------------- ")

    except:
        ex = "🐞 Some error occured during generation . Please review your code"
        raise Exception(ex)
