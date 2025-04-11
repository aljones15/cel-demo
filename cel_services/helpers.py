from yaml import load as load_yaml

def load_settings(settings_file):
    stream_doc = open(settings_file, "r")
    return load_yaml(stream_doc)
