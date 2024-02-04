import yaml
def getTheme():
    with open("source/config/config.yaml", "r") as stream:
        x = (yaml.safe_load(stream))
        return x['Theme']
class Theme:
  def __init__(self, theme_name):
    self.colourDict = {'ColourBlind': {'text_color': 'blue', 'background_color': 'white'}, 'Normal': {'text_color': 'yellow', 'background_color': 'red'}, 'Test': {'text_color': 'green', 'background_color': 'purple'}, 'Default': {}}
    self.theme_name = theme_name
  def getColor(self):
    return self.colourDict[self.theme_name]
