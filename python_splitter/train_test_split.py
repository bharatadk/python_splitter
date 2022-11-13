import os
import glob
import numpy as np
import shutil
import re


class Train_test_split_class(object):
    def __init__(self):
        self.root_folder = ""
        self.new_root = "Train_Test_Folder"
        self.classes = []
        self.train_per = 0
        self.test_per = 0
        self.val_per = 0

    # class methods

    def generate_classes(self):
        self.classes = [
            name
            for name in os.listdir(self.root_folder)
            if os.path.isdir(os.path.join(self.root_folder, name))
            and name != "__pycache__"
        ]

    def path_validation(self):

        isExist = os.path.exists(self.root_folder)
        if isExist:

            return
        raise Exception("🐞The SOURCE PATH doesn't exits")

    def make_directories(self):

        if os.path.exists(self.new_root):
            shutil.rmtree(self.new_root)
        for cls in self.classes:
            os.makedirs(os.path.join(self.new_root, "train", cls))
            os.makedirs(os.path.join(self.new_root, "test", cls))

            if self.val_per > 0:
                os.makedirs(os.path.join(self.new_root, "val", cls))

        return

    def validation_per(self):

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

        ## creating partition of the data after shuffeling
        for cls in self.classes:
            src = os.path.join(self.root_folder, cls)  # root_folder to copy images from

            allFileNames = os.listdir(src)

            np.random.shuffle(allFileNames)

            ## E.g.here 0.75 = training ratio , (0.95-0.75) = validation ratio , (1-0.95) =
            ##training ratio

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

            # #Converting file names from array to list

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




