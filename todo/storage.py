from pathlib import Path
from platformdirs import user_data_dir

DATA_DIR = Path(user_data_dir("todo-cli"))
DATA_FILE = DATA_DIR / "data.json"
