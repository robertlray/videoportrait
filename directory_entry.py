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
            return 'This is not a directory.'
        # List the files in the directory
        dirlist = os.listdir(self.pathname)
        # For every item that ls returns, make new directory
        # entry object and stick into children list.
        for entry in dirlist:
            z = directory_entry(pathname = self.pathname + entry)  
            self.children.append(z)
            if z.is_directory() == True:
                z.find_children()
        return True

    def print_children(self, recurse = False, filetype = False, headers = False):
        for child in self.children:
            if child.pathname.endswith('.py') and filetype == 'python':
                print child.pathname
            elif filetype == 'python' and not child.pathname.endswith('.py'):
                return None
            if child.is_file() and headers == True:
                y = open(child.pathname)
                print y.readline()
                y.close()
            else:
                print child.pathname
                if child.is_directory() and recurse == True:
                    child.print_children()
            
            
       

        

