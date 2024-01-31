import yaml
def getTheme():
    with open("source/config/config.yaml", "r") as stream:
        x = (yaml.safe_load(stream))
        return x['Theme']
class Theme:
  def __init__(self, theme_name):
    self.colourDict = {'ColourBlind': 'blue', 'Normal': 'red', 'Test': 'yellow', 'Default': 'default'}
    self.theme_name = theme_name
  def getColor(self):
    return self.colourDict[self.theme_name]
