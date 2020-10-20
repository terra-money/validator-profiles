import glob
import re
import codecs

from jinja2 import Template
from jigu import Terra
from pathlib import Path

cwd = Path(__file__).parent.absolute()
terra = Terra("columbus-4", "https://lcd.terra.dev")
pattern = re.compile(r"terravaloper[a-zA-Z0-9]{39}")
paths = glob.glob(str(Path.joinpath(cwd.parent, "validators")) + "/*")
delegates = terra.delegates()

validators = []
for path in paths:
    address = pattern.search(path).group(0)
    if address in delegates:
        validator = {
            "address": address,
            "moniker": delegates[address].info.description.moniker,
        }
        validators.append(validator)

with codecs.open(cwd / "README.md.jinja", encoding="utf-8") as f:
    template = Template(f.read())
    with open(cwd.parent / "README.md", "w") as readme:
        readme.write(
            template.render(validators=sorted(validators, key=lambda x: x["moniker"]))
        )