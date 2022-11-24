def file_finder(dirs, file_name):
    # print(f"Current directory {dirs[0]} contains {dirs[1]}")
    # print("dirs1 = ", dirs[1])
    for subdir in dirs[1]:
        if type(subdir) == tuple:
            # print("subdir = ", subdir, "\n")
            path = file_finder(subdir, file_name)
            if path:
                print()
                return subdir[0] + "/" + path
        else:
            if subdir == file_name:
                return dirs[0] + "/" + file_name


dirs1 = ("home", [
            ("Documents", [
                ("FP", [
                    "lists.txt", 
                    "recursion.pdf", 
                    "functions", 
                    "tmp.txt" ]), 
                ("Python", [
                    "hello_world.py", 
                    "readme.md" ])]), 
            ("Downloads", [
                ("Movies", [
                    ("TV Series", [
                        "BreakingBad.mp4", 
                        "TheBigBangTheory.avi" ]), 
                    "1.avi", 
                    "22", 
                    "001.mp4"])]), 
            "tmp.txt", 
            "page.html"])

dirs2 = ("Movies", [
            ("TV Series", [
                "BreakingBad.mp4", 
                "TheBigBangTheory.avi" ]), 
            "1.avi", 
            "22", 
            "001.mp4"])

print(file_finder(dirs1, 'hello_world.py'))