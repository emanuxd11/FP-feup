def file_finder(dirs, file_name):
    # dirname will be the name of our current parent
    # directory and files will be the list of files, 
    # including other directories, that it may contain
    dirname, files = dirs
    
    # we iterate through each subdirectory in the files
    # list until we get to one that isn't a directory
    for subdir in files:
        # we must then check if the subdir 
        # variable is of type tuple
        if type(subdir) == tuple:
            # it being a tuple means we've got more
            # subdirectories to go through, hence
            # the recursive call to our find function
            path = file_finder(subdir, file_name)
            if path:
                # if the path variable doesn't evaluate to 
                # "None", we know we've found the file and
                # therefore we add the name of our current
                # directory to the file path
                return f"{dirname}/{path}"

        # when it isn't a tuple, we have reached the point
        # where we only have files in the current directory
        else:
            # at this point we check if the name of
            # out current file matches the name of 
            # the file we're looking for
            if subdir == file_name:
                # if it does we return the name of our current
                # plus the name of our file separated by a "/" 
                return f"{dirname}/{file_name}"


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

print(file_finder(dirs1, "hello_world.py"))