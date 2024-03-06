import yaml
def getLanguage():
    with open('source/config/config.yaml', 'r') as config_file:
        yaml_file = yaml.safe_load(config_file)
        language = yaml_file['Language']
    return language