#!/usr/bin/env python3

import shutil
import os
os.chdir('/home/student/mycode')
# the following line will move a file.
shutil.move('raynor.obj', 'ceph_storage/')
xname = input('What is the new name for kerrigan.obj??')
# the following line will rename a file.
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
