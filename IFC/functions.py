import os.path

def get_trashbin_rename(path, fname):
    attempt = os.path.join(path, 'deleted')
    attempt = os.path.join(attempt, fname)
    while os.path.isFile(fname):
        fname = '_' + fname
    return fname