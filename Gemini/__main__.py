import glob
import logging

from pathlib import Path
from Gemini.utils import load_plugins
from Gemini import *

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Gemini/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

txt = f"Your TOKEN: {TOKEN}\n"
txt += f"Your G-API_KEY: {GEMINI_API_KEY}\n\n"
txt += "Bot Started"
print(txt)

if __name__ == "__main__":
    bot.run_until_disconnected()
