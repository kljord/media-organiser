from Media import Media
from FileUtils import FileUtils
from glob import glob
from os.path import join

class Runner:

    def __init__(self, args):
        self.sourcePath = args[1]
        self.destinationPath = args[2]
        self.filesRenamed = 0
        self.filesToRename = self.__getMaxNumberOfFilesToRename(args)

    def run(self):
        for file in self.__filesToRename():
            self.__checkFilesRenamed()
            self.__rename(file)

    def __getMaxNumberOfFilesToRename(self, args):
        if (len(args) == 4):
            return args[3]
        else:
            return 1000

    def __filesToRename(self):
        return glob(join(self.sourcePath, "*"))

    def __checkFilesRenamed(self):
        if (self.filesRenamed == self.filesToRename):
            exit(0)
        self.filesRenamed = self.filesRenamed + 1

    def __rename(self, file):
        media = Media(file)
        FileUtils.mv(media, self.destinationPath)