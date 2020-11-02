from sortRule import SortRule

TRACKED_FOLDERS = []

SORT_RULES = [
    SortRule("/home/h/Downloads/img", "ext", [".jpeg", ".jpg", ".png", ".psd"]), #Images
    SortRule("/home/h/Downloads/compressed", "ext", [".zip", ".7zip", ".rar"]) #Compressed
]