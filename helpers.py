from yaml import CLoader, load as load_yaml
from os import getcwd

def load_settings(settings_file):
    settings_path = getcwd() + "/" + settings_file
    stream_doc = open(settings_path, "r")
    return load_yaml(stream_doc, Loader=CLoader)
