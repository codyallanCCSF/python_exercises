# Analyst class declaration

class Analyst:
    
    # Liks Manager to Analyst
    def link_manager(self, manager_instance):
        self.manager = manager_instance

    # Method to test link
    def verify_analyst(self):
        return f"Analyst Handshake: {self.manager.system_status}"

    def count_report(self):
        
        # Count variables assigned with
        # chain accessors len(analyst -> manager -> list)
        fiction_count = len(self.manager.fiction)
        nonfiction_count = len(self.manager.nonfiction)

        return f"""
        ----- Report -----
        Fiction: {fiction_count}
        Non-Fiction: {nonfiction_count}
        """

    def find_title(self, title):
        
        # Concatenate both lists of books
        books = self.manager.fiction + self.manager.nonfiction
        
        for book in books:
            if title.lower() == book["title"].lower():
                return f"""                
    Title: {book["title"]}
    Author: {book["author"]}
    Price: ${book["price"]}
    Description: {book["info"]["description"]}
    """
        return "Book not found"

    # FIXME Description format
