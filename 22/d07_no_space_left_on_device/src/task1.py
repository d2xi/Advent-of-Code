import re
from abc import ABC, abstractmethod


def get_reclaimable_space(console_history, max_size=1E5):
    dtb = DirectoryTreeBuilder(console_history)
    index = dtb.dir_size_index
    filtered_directories = [v for v in index.values() if v <= int(max_size)]
    reclaimable_space = sum(filtered_directories)
    return reclaimable_space


class Node(ABC):

    def __init__(self, path):
        self._path = path
        self._parent = None
        self._size = None

    @property
    @abstractmethod
    def size(self):
        pass

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, obj):
        if not isinstance(obj, Directory):
            raise TypeError(
                f"Expected type Directory, but received {type(obj)}")
        self._parent = obj


class File(Node):

    def __init__(self, path, size):
        super().__init__(path)
        self._size = size

    @property
    def size(self):
        return self._size


class Directory(Node):

    def __init__(self, path):
        super().__init__(path)
        self._subnodes = {}
        self._subdirectories = {}

    def add(self, obj):
        self._subnodes[obj.path] = obj
        if isinstance(obj, Directory):
            self.subdirectories[obj.path] = obj

    def get(self, path):
        if path not in self._subnodes:
            raise KeyError(
                f"The object '{path}' was not found under {self.path}")
        return self._subnodes.get(path)

    @property
    def subdirectories(self):
        return self._subdirectories

    @Node.size.getter
    def size(self):
        if self._size == None:
            sizes = [int(node.size) for node in self._subnodes.values()]
            self.size = sum(sizes)
        return self._size


class DirectoryTreeBuilder():

    def __init__(self, console_history):
        self._root = None
        self._dir_size_index = {}
        self.parse_console_history(console_history)
        self.build_directory_size_index()

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, dir):
        self._root = dir

    @property
    def dir_size_index(self):
        return self._dir_size_index

    def parse_console_history(self, console_history):

        PATTERN_CMD_CD_DOWN = re.compile(
            r"\$ cd (?P<dir>(?:/|[a-zA-Z]+.?[a-zA-Z]*))")
        PATTERN_CMD_CD_UP = re.compile(r"\$ cd ..")
        PATTERN_CMD_LS = re.compile(r"\$ ls")

        PATTERN_FILE = re.compile(r"(?P<size>\d+) (?P<name>.+)")
        PATTERN_DIR = re.compile(r"dir (?P<name>.+)")

        PATTERN_COMMANDS = r'(?:(?:^\$ .*\n)'
        PATTERN_OUTPUT = r'(?:^(?!\$).*(?:\n|$))+)'

        #re.complie(r"(?:^\$ .*|^(?!\$).*(?:\n(?!\$).*)*$(?:\n|$))")

        PATTERN_IN_OUT = re.compile(
            rf'{PATTERN_COMMANDS}|{PATTERN_OUTPUT}', re.MULTILINE)
        iter_matches = iter(re.findall(PATTERN_IN_OUT, console_history))

        curr_path = []

        def pwd(name=''):
            components = [*curr_path, name] if name else curr_path
            return '/'.join(components).replace("//", '/')
        wd = None

        for console_io in iter_matches:
            if PATTERN_CMD_CD_DOWN.match(console_io):
                curr_dir = PATTERN_CMD_CD_DOWN.match(console_io).group('dir')
                curr_path.append(curr_dir)
                if wd == None:
                    self.root = Directory(pwd())
                    wd = self.root
                else:
                    wd = wd.get(pwd())
            elif PATTERN_CMD_CD_UP.match(console_io):
                curr_path.pop()
                wd = wd.parent
            elif PATTERN_CMD_LS.match(console_io):
                output = next(iter_matches).split('\n')
                for entry in output:
                    if PATTERN_DIR.match(entry):
                        name = PATTERN_DIR.match(entry).group('name')
                        dir_node = Directory(pwd(name))
                        dir_node.parent = wd
                        wd.add(dir_node)
                    elif PATTERN_FILE.match(entry):
                        name = PATTERN_FILE.match(entry).group('name')
                        size = PATTERN_FILE.match(entry).group('size')
                        file_node = File(pwd(name), size)
                        file_node.parent = wd
                        wd.add(file_node)

    def build_directory_size_index(self):
        # dfs
        visit_stack = list()
        visit_stack.append(self.root)
        while visit_stack:
            cd = visit_stack.pop()
            name = cd.path
            self.dir_size_index[name] = cd.size
            visit_stack += cd.subdirectories.values()
