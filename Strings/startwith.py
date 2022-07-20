import os

filenames = os.listdir(".")

print(filenames)


print(any(name.endswith(".py") for name in filenames))
