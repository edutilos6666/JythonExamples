class Readable:
    def is_readable(self):
        pass

    def read(self):
        pass


class Writable:
    def is_writable(self):
        pass

    def write(self):
        pass


class Executable:
    def is_executable(self):
        pass

    def execute(self):
        pass


class CustomFile(Readable, Writable, Executable):
    def __init__(self, filename):
        self.filename = filename

    def is_readable(self):
        return ".read" in self.filename

    def read(self):
         if self.is_readable():
             print("{0} was read.".format(self.filename))
         else:
             print("{0} is not readable.".format(self.filename))


    def is_writable(self):
        return ".write" in self.filename

    def write(self):
        if self.is_writable():
            print("{0} was written.".format(self.filename))
        else:
            print("{0} is not writable.".format(self.filename))



    def is_executable(self):
        return ".exe" in self.filename

    def execute(self):
        if self.is_executable():
            print("{0} was executed".format(self.filename))
        else:
            print("{0} is not executable.".format(self.filename))


