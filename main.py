import urllib.request
import tempfile
import colorama
from tqdm import tqdm
import os
import shutil
import time

colorama.init()

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

print("##################################################")
print("#                                                #")
print("#           JKinc Element Sound Fixer            #")
print("#                                                #")
print("##################################################")
print("\nPress Enter To Continue.")

input("")

print(colorama.Fore.LIGHTRED_EX, end="")

print("Closing Element",)
os.system('taskkill /IM "Element.exe" /F > nul')

print(colorama.Fore.RESET, end="")

time.sleep(2)

print(colorama.Fore.LIGHTGREEN_EX, end="")

print("Searching for element directory...")

print(colorama.Fore.RESET, end="")

if not os.path.exists(os.path.join(os.getenv("LOCALAPPDATA"), "element-desktop")):
    print(colorama.Fore.LIGHTGREEN_EX, end="")
    print("\nElement Not Detected on this Computer")
    print("Press Enter To Quit")
    print(colorama.Fore.RESET, end="")
    input("")
    exit(1)


major = 0
minor = 0
patch = 0

for i in os.listdir(os.path.join(os.getenv("LOCALAPPDATA"), "element-desktop")):
    if "app-" in i:
        (ma, mi, pa) = i.replace("app-", "").split(".")
        ma = int(ma)
        mi = int(mi)
        pa = int(pa)
        if ma > major:
            major = ma
            if mi > minor:
                minor = mi
                if pa > patch:
                    patch = pa


pathtodata = os.path.join(os.getenv("LOCALAPPDATA"), "element-desktop", "app-" + str(ma) + "." + str(mi) + "." + str(pa), "resources", "webapp.asar")

tempdir = tempfile.mkdtemp()

try:
    os.remove(os.path.join(os.getenv("LOCALAPPDATA"), "element-desktop", "app-" + str(ma) + "." + str(mi) + "." + str(pa), "resources", "webapp.asar.old"))
except:
    pass

os.rename(pathtodata, os.path.join(os.getenv("LOCALAPPDATA"), "element-desktop", "app-" + str(ma) + "." + str(mi) + "." + str(pa), "resources", "webapp.asar.old"))

print(colorama.Fore.LIGHTGREEN_EX, end="")

print("Backing up original data")

print(colorama.Fore.RESET, end="")

print("Downloading Patch")
print(colorama.Fore.RESET, end="")

file = tempfile.NamedTemporaryFile(delete=False)
name = file.name
file.close()

with DownloadProgressBar(unit='B', unit_scale=True,
                            miniters=1, desc="Progress") as t:
        urllib.request.urlretrieve("https://github.com/JKincorperated/Element-Discord-Sounds/raw/main/webapp.asar", filename=name, reporthook=t.update_to)

print(colorama.Fore.LIGHTGREEN_EX, end="")

print("Installing Patch")

print(colorama.Fore.RESET, end="")

shutil.copyfile(name, pathtodata)

print(colorama.Fore.LIGHTGREEN_EX, end="")
print("Complete!")
input("Press Any Key To Exit")
