import glob
import logging

from pathlib import Path
from Gemini.utils import load_plugins
from Gemini import bot

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Gemini/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Bot started!")

if __name__ == "__main__":
    bot.run_until_disconnected()
