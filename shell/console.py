import code
import sys
from pathlib import Path
import os

def get_available_path(path:Path, name=None, index=0) -> Path:
    if os.path.exists(path):
        i = index + 1
        add_version = f"({i})"
        filename = path.stem if name == None else name
        new_filename = f"{filename} {add_version}{path.suffix}"
        
        return get_available_path(path.with_name(new_filename), name=filename, index=i)
    return path

class MyInteractiveConsole(code.InteractiveConsole):
    def __init__(self, locals=None):
        self.commands_path = get_available_path(Path('commands.txt'))
        super().__init__(locals)

    def push(self, line):
        super().push(line)
        self.log_file = open(self.commands_path, "a")
        self.log_file.write(line + '\n')
        self.log_file.close()
        
console = MyInteractiveConsole()

if __name__ == "__main__":
    console.interact()