import os
if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")
    print("done")
else:
    print("The file does not exist")