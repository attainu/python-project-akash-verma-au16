from entities.extension import OrganiseFilesWithExtension
from entities.last_modified import OrganiseFilesWithLastModified
from entities.recently_used import OrganiseFilesWithRecentlyUsed
from entities.size import OrganiseFilesWithSize


class OrganiseMethod:
    def __init__(self, path, method):
        self.path = path
        self.method = method
        self.selection(self.method)

    def selection(self, method):
        if method == 'extension':
            call_extension_method = OrganiseFilesWithExtension()
            call_extension_method.extensionSort(self.path)

        elif method == 'size':
            call_size_method = OrganiseFilesWithSize()
            call_size_method.sizeSort(self.path)

        elif method == 'last_modified':
            call_last_modified_method = OrganiseFilesWithLastModified()
            call_last_modified_method.lastModifiedSort(self.path)

        elif method == 'recently_used':
            call_recently_used_method = OrganiseFilesWithRecentlyUsed()
            call_recently_used_method.recentlyUsedSort(self.path)

        else:
            pass
