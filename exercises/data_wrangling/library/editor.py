# Editor class declaration

class Editor:

    # Links Manager to Editor
    def link_manager(self, manager_instance):
        self.mgr = manager_instance

    # Method to test link
    def verify_editor(self):
        return f"Editor Handshake: {self.manager.system_status}"
