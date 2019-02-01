import subprocess as sp
import re


class modudator():
    def __init__(self):
        self.check_version()

    def check_version(self):
        sp.call('pip list -o > modulesToBeUpdated.txt', shell=True)
        with open("modulesToBeUpdated.txt") as mtbu:
            ind = 0
            mods_to_be_updated = []
            for line in mtbu.readlines():
                ind += 1
                if ind < 3:
                    continue
                line = self.edit_line(line)
                mods_to_be_updated.append(line)
        print(mods_to_be_updated)
        for mod in mods_to_be_updated:
            print('\n{0} is updating\n'.format(mod.upper()))
            self.update_module(mod)
        print('Done!!')

    def update_module(self, des_mod):
        sp.call(
            'python -m pip install --upgrade {0}'.format(des_mod), shell=True)

    def edit_line(self, des_line):
        des_line = re.sub('[0-9.]', '', des_line)
        des_line = des_line.replace('wheel', '')
        des_line = des_line.replace('sdist', '')
        des_line = des_line.strip()
        return des_line


if __name__ == "__main__":
    modudator()
