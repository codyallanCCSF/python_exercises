# Import all classes

from manager import Manager
from editor import Editor
from analyst import Analyst

# Import data

from book_datasets import fiction_books, nonfiction_books

def main():
    
    # Create each object
    manager_obj = Manager()
    editor_obj = Editor()
    analyst_obj = Analyst()

    # Give Manager access to book data
    manager_obj.fiction = fiction_books
    manager_obj.nonfiction = nonfiction_books
    
    # Link Analyst to Manager
    analyst_obj.link_manager(manager_obj)
    
    # Calls count_report() method and prints result
    print(analyst_obj.count_report())

if __name__ == "__main__":
    main()
