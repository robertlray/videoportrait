import os

class directory_entry:

    def __init__(self, pathname = ""):
        self.pathname = ""
        self.children = list()
        self.pathname = pathname
        if self.is_directory():
            if self.pathname.endswith('/') == False:
                self.pathname = pathname + '/'

    def containing_directory(self):
        if self.pathname.endswith('/'):
            (x,y,z) = self.pathname.rstrip('/').rpartition('/')
            return x
        else:
            (x,y,z) = self.pathname.rpartition('/')
            return x

    def is_file(self):
        return os.path.isfile(self.pathname)

    def is_directory(self):
        return os.path.isdir(self.pathname)
    
    def find_children(self):
        # If this isn't a directory, return FALSE
        if self.is_directory() == False:
            return False
        # If this is a directory, continue

        # List the files in the directory
        dirlist = os.listdir(self.pathname)

        # For every item that ls returns, make new directory
        # entry object and stick into children list.
        for entry in dirlist:
            z = directory_entry(pathname = self.pathname + entry)
            z = directory_entry(pathname = self.pathname + entry)    
            self.children.append(z)
            if z.is_directory() == True:
                z.find_children()
        return True

    def print_children(self, recurse = False):
        for child in self.children:
            print child.pathname
            if child.is_directory() and recurse == True:
                child.print_children()

    def print_python_children(self):
        # same as print_children with few changes
        # just setting two paramaters - needs to either be a directory
        # or a .py file
        for child in self.children:
            if child.is_directory():
                print child.pathname
            elif child.pathname.endswith('.py'):
                print child.pathname

    def read_file(self):
        # Find all python files
        for child in self.children:
            if child.pathname.endswith('.py'):
                 # Open the python file
                y = open(child.pathname)
                 # print out 1000 bytes of each python file within the terminal
                for line in y.readlines(1000):
                    print line
                 # close file 
                y.close()
        

