import string

class Logger :
    File: string
    def __init__(self, File:string ):
        self.File= File
    def Log(self,Information):
        print("Logging information : " + Information)
        file = open(self.File,"a")
        file.write(Information)
        file.close()


        