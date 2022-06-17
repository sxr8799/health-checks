#!/usr/bin/env python3

import os
import shutil
import sys

def check_reboot():
    """Returns True if computer has a pending reboot."""
    return os.path.exist("/run/reboot-required")

def check_disk_usage(disk, min_gb, min_percent):
    """Returns True if there is enough disk space, fale otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return False
    return True

def main():
    if check_reboot():
        print("Pending Reboot")
        sys.exit(1)
    # Check for at least 2 GB and 10% free
    if check_disk_usage(disk="/",min_gb=2,min_percent=10):
        print("Disk full.")
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)

main()
