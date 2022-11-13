import os
import glob
import numpy as np
import shutil
import re

class Image_grouping_class(object):
    def __init__(self):
        self.root_folder = ""
        self.new_source = "NEW_SOURCE_FOLDER"
        self.all_files = []
        self.all_image_files = []
        self.classes = []
        self.allowed_extensions = (
            ".jpg",
            ".png",
            ".jpeg",
            ".bmp",
            ".raw",
            ".tiff",
            ".svg",
            ".tif",
            ".gif",
            ".heif",
            "webp",
        )

    def generate_classes(self):

        self.all_files = os.listdir(root_folder)
        mapper = {}

        for file in self.all_files:
            if file.endswith(allowed_extensions):
                self.all_image_files.append(file)

                file = file.split(".")[0]
                class_name = re.findall(r".*\D", file)[0]

                if class_name not in mapper:
                    mapper[class_name] = 1

        self.classes = list(mapper.keys())

        del self.all_files

    def make_directories(self):

        # Remove previous "NEW_SOURCE_FOLDER" if exists
        if os.path.exists(self.new_source):
            shutil.rmtree(self.new_source)

        for cls in self.classes:
            os.makedirs(os.path.join(self.new_source, cls))

    def copy_files(self):

        for file in self.all_image_files:
            file_name_without_extension = file.split(".")[0]
            folder_to_copy_to = re.findall(r".*\D", file_name_without_extension)[0]
            shutil.copy(
                os.path.join(self.root_folder, file),
                os.path.join(self.new_source, folder_to_copy_to),
            )




def image_to_class(root_folder_path):

    try:

        obj = Image_grouping_class()

        obj.root_folder = root_folder_path

        obj.generate_classes()
        print("✅All Classes Scanned...")

        obj.make_directories()
        print("✅All Directories Created...")

        obj.copy_files()
        print("✅All Images Copied...")

        print("\n-------------Successful !!!--------------- ")

    except:

        ex = "🐞 Some error occured during generation . Please review your code"
        raise Exception(ex)
