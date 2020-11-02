from sortRule import SortRule

TRACKED_FOLDERS = []

SORT_RULES = [
    SortRule("/img", "ext", [".jpeg", ".jpg", ".png", ".psd"]), #Images
    SortRule("/compressed", "ext", [".zip", ".7zip", ".rar"]) #Compressed
]