import os


class directory_entry:
    pathname = ""
    children = list()

    def __init__(self, pathname = ""):
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
        # Python equivalent of ls
        dirlist = os.listdir(self.pathname)
        # For every item that ls returns, make new directory
        # entry object and stick into children list.
        for dir in dirlist:
            z = directory_entry(pathname = self.pathname + dir)
            z.find_children()
            self.children.append(z)
        return True

    def print_children(self):
        for child in self.children:
            print child.pathname
           #  if self.is_file():
           #      print child.pathname
           #  elif self.is_directory():
           #      child.print_children()
