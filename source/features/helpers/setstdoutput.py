import sys
import datetime
from datetime import datetime
def fixStdout():
    today = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    filename = "log_" + today
    sys.stdout = open(f"source/logs/{filename}", "w")
