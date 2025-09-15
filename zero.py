# the brains
import sys
from modules.task_manager import TaskManager
from modules.notifier import Notifier
from modules.research import Research
from modules.personality import Personality

def main():
    print("At your service, ma'am")

# Initialize modules
tasks = TaskManager()
notifier = Notifier()
research = Research()
personality = Personality()

while True: 
        command = input(">>>").lower()
        if command in ["quit exit q"]:
            print("Goodnight maam")
            sys.exit()

