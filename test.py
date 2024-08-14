class TreeNode:
    def __init__(self, data=None):
        self.__data = data
        self.__left = None
        self.__right = None

    def __del__(self):
        print('data {} is deleted'.format(self.__data))
        