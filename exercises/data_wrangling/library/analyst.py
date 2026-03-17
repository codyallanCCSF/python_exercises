# Analyst class declaration

class Analyst:
    
    # Liks Manager to Analyst
    def link_manager(self, manager_instance):
        self.mgr = manager_instance

    # Method to test link
    def verify_analyst(self):
        return f"Analyst Handshake: {self.mgr.system_status}"
