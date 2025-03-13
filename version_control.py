from friendsbalt.acs import OrderedMap, StringDiff, AVLTree

# save versions of file
# store version history of multiple files
# restore previous version
# see a log of changes

class VersionControl:
    def __init__(self, text):
        om = OrderedMap()
        

        
    def save_version(self, text):
        pass

    def restore_version(self):
        pass

    def display_log(self):
        pass

    
    

    class Node:
        pass


a = "apple"
b = "apple!!"
diff = StringDiff(a, b)
str = StringDiff.serialize(diff)
print(str)

deserialized = StringDiff.deserialize(str)
print(deserialized)
