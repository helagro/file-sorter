Run with "python main.py" - python3 doesn't work for me

env.py example:

from sortRule import SortRule
TRACKED_FOLDERS = ["/media/home/dir", "/media/home/anotherDir"]
SORT_RULES = [
    SortRule("/media/home/folderToMoveTo", "ext", [".cpp", ".c"])
]