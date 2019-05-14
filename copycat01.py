#!/usr/bin/env python3

import shutil
import os
os.chdir("/home/student/mycode/")
#the following line will create back up file
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#the following line will create a directory if it does not exist
shutil.copytree("5g_research/", "5g_research_backup/")
