from pathlib import Path 
from argparse import ArgumentParser
import subprocess

from common import exdir
exdir=Path(exdir)

p = ArgumentParser()
p.add_argument("--hash", type=str)
args = p.parse_args()

base = Path(__file__).parent

def apply(file: Path):
    print(file.read_text())
    subprocess.check_output(f"cd {exdir} && git apply {file}", shell=True)

if args.hash:
    for patch in base.glob("*.patch"):
        hashed, timestamp, version = patch.with_suffix("").name.split("_")
        if hashed == args.hash: 
            apply(patch)
            break
else:
    latest = 0
    latest_patch = None 
    for patch in base.glob("*.patch"):
        hashed, timestamp, version = patch.with_suffix("").name.split("_")
        if int(timestamp) > latest:
            latest = int(timestamp)
            latest_patch = patch 
    apply(latest_patch)
