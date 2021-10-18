def read(filename):
    return open(filename, "r").read()


def write(filename, content):
    open(filename, "w").write(content)
