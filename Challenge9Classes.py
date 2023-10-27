class LibraryItemInfo:
    def __init__(self, ItemName, Author, Publisher):
        self.ItemName = ItemName
        self.Author = Author
        self.Publisher = Publisher

    def get_ItemName(self):
        return self.ItemName

    def get_Author(self):
        return self.Author

    def get_Publisher(self):
        return self.Publisher

    def set_ItemName(self, string):
        self.ItemName = string

    def set_Author(self, string):
        self.Author = string

    def set_Publisher(self, string):
        self.Publisher = string


class Book:
    def __init__(self, Title, Author, Publisher, Pages, IsHardCopy, IsEbook):
        self.Title = Title
        self.Author = Author
        self.Publisher = Publisher
        self.Pages = Pages
        self.IsHardCopy = IsHardCopy
        self.IsEbook = IsEbook

    def get_Title(self):
        return self.Title

    def get_Author(self):
        return self.Author

    def get_Publisher(self):
        return self.Publisher

    def get_Pages(self):
        return self.Pages

    def get_IsHardCopy(self):
        return self.IsHardCopy

    def get_IsEbook(self):
        return self.IsEbook

    def set_Title(self, string):
        self.Title = string

    def set_Author(self, string):
        self.Author = string

    def set_Publisher(self, string):
        self.Publisher = string

    def set_Pages(self, integer):
        self.Title = integer

    def set_IsHardCopy(self, boolean):
        self.IsHardCopy = boolean

    def set_IsEbook(self, boolean):
        self.IsEbook = boolean
