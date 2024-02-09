from pathlib import Path 
from time import time 
from hashlib import sha1
import subprocess

from common import exdir
exdir=Path(exdir)

base = Path(__file__).parent
version = ""
for line in (exdir / "gdre_export.log").read_text().splitlines():
    if line.startswith("Version: "):
        version = line.split("Version: ")[1]
        break


def run_cmd(cmd):
    # print(cmd)
    return subprocess.check_output(cmd, shell=True)

if gitdiff := run_cmd(f"cd {exdir} && git diff"):
    patch_hashed = sha1(gitdiff).hexdigest()
    for patch in base.glob("*.patch"):
        hashed, timestamp, version = patch.with_suffix("").name.split("_")
        if patch_hashed == hashed:
            print(f"{patch} already exists, exiting...")
            break
    else:
        timestamp = int(time())
        patch_file = base/f"{patch_hashed}_{timestamp}_{version}.patch"
        if patch_file.is_file():
            exit(1)
        print(f"writing patch {patch_file.name}")
        patch_file.write_bytes(gitdiff)
        print(run_cmd(f"cd {base} && git add . && git commit -am \"{timestamp}\" && git push").decode())
else:
    print("No changes detected!")