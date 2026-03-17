# Import all classes

from manager import Manager
from editor import Editor
from analyst import Analyst

def main():
    
    # Create each object
    manager_obj = Manager()
    editor_obj = Editor()
    analyst_obj = Analyst()

    # Pass manager_obj to other objects
    editor_obj.link_manager(manager_obj)
    analyst_obj.link_manager(manager_obj)

    # Verify Handshake
    print(editor_obj.verify_editor())
    print(analyst_obj.verify_analyst())

if __name__ == "__main__":
    main()
