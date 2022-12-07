
def build_vfs(input: str):
    cur = root = VfsDir(None, '/')
    for line in input.splitlines():
        cmd = line.replace('$ ', '').split(' ')
        if cmd[0] == 'cd':
            if cmd[1] == '/':
                cur = root
            elif cmd[1] == '..':
                cur = cur.parent
            else:
                cur = cur.get_dir(cmd[1])
        elif cmd[0] == 'dir':
            cur.add_dir(cmd[1])
        elif cmd[0].isnumeric():
            cur.add_file(cmd[1], int(cmd[0]))
    return root

class VfsDir:
    def __init__(self, parent: 'VfsDir', path: str) -> None:
        self.parent = parent
        self.path = path
        self.dirs: list['VfsDir'] = []
        self.files: list['VfsFile'] = []

    def add_dir(self, path: str) -> 'VfsDir':
        d = VfsDir(self, path)
        self.dirs.append(d)
        return d

    def get_dir(self, path) -> 'VfsDir':
        for d in self.dirs:
            if d.path == path:
                return d
        return None

    def add_file(self, name: str, size: int) -> 'VfsFile':
        f = VfsFile(self, name, size)
        self.files.append(f)
        return f

    def size(self) -> int:
        fsize = sum([f.size for f in self.files])
        dsize = sum([d.size() for d in self.dirs])
        return fsize + dsize

    def size_list(self, sizes: list[int]) -> list[int]:
        sizes.append(self.size())
        for d in self.dirs:
            d.size_list(sizes)
        return sizes

class VfsFile:
    def __init__(self, dir: VfsDir, name: str, size: int) -> None:
        self.dir = dir
        self.name = name
        self.size = size
