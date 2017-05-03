import os.path
import sys
sys.path.append('../utils')
from utils.FileUtils import FileUtils

class PictureShrinker:

    def __init__(self, file, destinationPath):
        self.sourceFilename = file.fullPath
        self.destinationFilename = self.__buildDestinationFilename(file, destinationPath)

    def shrink(self):
        FileUtils.copy(self.sourceFilename, self.destinationFilename)

    def __buildDestinationFilename(self, file, destinationPath):
        return os.path.join(destinationPath, file.partialPath, file.name)
