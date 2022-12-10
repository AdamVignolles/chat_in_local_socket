import easygui

path = easygui.fileopenbox()

class files:
    def __init__(self, path):
        self.path = path
    def read(self):
        with open(self.path, 'rb') as file:
            return file.read()
    def write(self, data):
        #add method if file not exist
        with open(self.path, 'wb') as file:
            file.write(data)