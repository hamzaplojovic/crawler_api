import os
import random

os.system("git checkout hamzaplojovic-patch-1")
with open("test.txt", "w") as f:
    f.write(str(random.randint(0, 10000000)))
os.system("git add .")
os.system("git commit -m 'fix'")
os.system("git push")
os.system("git checkout master")
os.system("git pull")
