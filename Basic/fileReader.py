class FileReader:

    def __init__(self):
        self.do_nothing = 0

    def printFile(self):
        print("Helllo World")

    def readFile(self, file):
        reader = open(file)
        try:
            print(reader.read())
            # Further file processing goes here
        finally:
            reader.close()

    def writeFile(self, file, info):
        self.f = open(file, "a")
        self.f.write(info + "\n")
        self.f.close()
