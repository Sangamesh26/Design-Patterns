from abc import ABC, abstractmethod

class ServerInterface(ABC):
    @abstractmethod
    def server_service(self):
        pass

class Server(ServerInterface):
    def server_service(self):
        print("Displays server info here")

class ProxyServer(ServerInterface):
    def __init__(self, request_from_region):
        self.server = Server()
        self.request_from_region = request_from_region
        
    def server_service(self):
        if self.request_from_region == "Pakistan":
            print("Not accessable")
        else:
            self.server.server_service()

if __name__ == "__main__":
    not_allowed_server_example = ProxyServer("Pakistan")
    not_allowed_server_example.server_service()
    
    server = ProxyServer("India")
    server.server_service()
    