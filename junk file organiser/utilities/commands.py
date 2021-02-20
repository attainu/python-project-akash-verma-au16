import os
import shutil


class Commands:
    def __init__(self, source, destination, duplicate):
        self.source = source
        self.destination = destination
        self.duplicate = duplicate

    def move(self):
        shutil.move(self.source, self.destination)

    def delete(self):
        os.remove(self.source)

    def create(self):
        os.mkdir(self.destination)

    def checkAndMove(self):
        if os.path.exists(self.destination):
            self.checkDuplicate()
        else:
            self.create()
            self.move()

    def checkDuplicate(self):
        if os.path.exists(self.duplicate):
            self.delete()
        else:
            self.move()
