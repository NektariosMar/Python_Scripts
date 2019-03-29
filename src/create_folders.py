import argparse
import os
import re


class Folder_Creator():

    def __init__(self):
        self.des_path, self.wantNumeric = self.get_cmd_args()
        print("self.des_path = {0}\nself.wantNumeric = {1}".format(self.des_path, str(self.wantNumeric)))
        self.list_of_names = self.get_name_list(self.wantNumeric)
        self.create_folders(self.des_path, self.list_of_names)
    
    def get_cmd_args(self):

        ret_path = ""
        ret_num = False
        
        cur_path = os.path.dirname(os.path.abspath(__file__))
        parser = argparse.ArgumentParser(description="Create either numeric folders either custom named folders")
        parser.add_argument("--outputDirectory", default=cur_path, help="Path to the output that will contain the newly created folders")
        parser.add_argument("-num","--numeric", action="store_true", help="Defines if the folders are going to have numeric or custom names")
        args = parser.parse_args()

        return args.outputDirectory, args.numeric

    def get_name_list(self, wants_numbered_names):

        ret_val = []
        num_of_folders = int(input("How many folders do you want to create? "))

        ret_val = ["0{0}".format(num + 1) if num < 9 else(num + 1) for num in range(num_of_folders)]
        
        if not wants_numbered_names:
            for index, name in enumerate(ret_val):
                user_name = self.get_user_input("Please type the name of the next folder: ")
                name = "{0}) {1}".format(name, user_name)
                # name = name.replace("[\\/:*?\"<>|]", "")
                name = re.sub("[\\\/:*?\"<>|]", "", name)
                name = name.replace(" ", "_")
                ret_val[index] = name

        
        for name in ret_val:
            print(name)
        
        return ret_val

    def create_folders(self, parent_path, fol_names):
        for index in range(len(fol_names)):
            try:
                if not os.path.exists(os.path.join(parent_path, fol_names[index])):
                    os.makedirs(os.path.join(parent_path, fol_names[index]))
            except OSError:
                print('Error: Creating directory {0}'.format(fol_names[index]))

    def get_user_input(self, message):
        # Support Python 2
        if sys.version_info >= (3, 0):
            return input(message)
        else:
            return raw_input(message)


if __name__ == "__main__":
    Folder_Creator()            
