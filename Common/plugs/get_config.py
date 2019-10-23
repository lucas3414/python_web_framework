import configparser
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')


class Config(object):

    def __init__(self, path):
        self.path = path
        self.cf = configparser.ConfigParser()
        self.cf.read(self.path, encoding='utf-8')

    def get(self, field, key):
        result = ""
        try:
            result = self.cf.get(field, key)
        except:
            result = ""
        return result

    def set(self, field, key, value):
        try:
            self.cf.set(field, key, value)
            self.cf.write(open(self.path, 'w'))
        except:
            return False
        return True


def r_config(config_file_path, field, key):
    rf = configparser.ConfigParser()
    try:
        rf.read(config_file_path, encoding='utf-8')
        result = rf.get(field, key)
    except:
        sys.exit(1)
    return result


def w_config(config_file_path, field, key, value):
    wf = configparser.ConfigParser()
    try:
        wf.read(config_file_path)
        wf.set(field, key, value)
        wf.write(open(config_file_path, 'w'))
    except:
        sys.exit(1)
    return True


if __name__ == '__main__':
    b = r_config(conf_dir, 'image', 'img_path')


