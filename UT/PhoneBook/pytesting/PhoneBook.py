import os

class PhoneBook:
    def __init__(self):
        self.entries = {}
        self.filename = "phonebook.txt"
        #self.file_cache = open(self.filename,"w")

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        return True

    def names(self):
        return self.entries.keys()

    def numbers(self):
        return self.entries.values()

    def clear(self):
        self.entries = {}
        #self.file_cache.close()
        #os.remove(self.filename)