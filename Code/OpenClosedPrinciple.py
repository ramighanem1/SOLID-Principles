#---------------
# wrong way
#---------------
# class StorageLocker():
#     def __init__(self,client) -> None:
#         self.client=client
#     def authenticate(self):
#         if self.client == 'AWS':
#             #some code
#             pass
#         elif self.client == 'Azure':
#             #some code
#             pass
#         elif self.client == 'GCP':
#             #some code
#             pass
#     def upload_file(self,filename):
#         if self.client == 'AWS':
#             #some code
#             pass
#         elif self.client == 'Azure':
#             #some code
#             pass
#         elif self.client == 'GCP':
#             #some code
#             pass


#---------------
# better way
#--------------- 
from abc import ABC,abstractmethod

class Auth(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class Uploader(ABC):
    @abstractmethod
    def upload_file():
        pass


class AWS(Auth,Uploader):
    def authenticate(self):
        #some code
        pass
    def upload_file(self,filename):
        #some code
        pass

class Azure(Auth,Uploader):
    def authenticate(self):
        #some code
        pass
    def upload_file(self,filename):
        #some code
        pass

class GCP(Auth,Uploader):
    def authenticate(self):
        #some code
        pass
    def upload_file(self,filename):
        #some code
        pass
    
