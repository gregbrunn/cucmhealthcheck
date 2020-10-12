# health.py
<p>Basic script that logs into CUCM using paramiko and pull down health check information. Writes results to text file.
Idea to do pre upgrade checks and maintains copy of results for anayalsis before upgrade and for reference post upgrade.</p>

This script requires python 
You will need to install the following packages 

#Note the following import statements any non basic python libray will need to be installed. 
import time
import sys
import threading
from ntpath import basename
import getpass
from multiprocessing.pool import ThreadPool
import itertools
import paramiko
from paramiko_expect import SSHClientInteraction
import os.path
import requests



<ol>
    <li>Pre 8.0 mode enabled</li>
    <li>Cluster securitu mode enable</li>
    <li>ITL Errors</li>
    <li>CTL Errors</li>
    <li>Backup History</li>
    <li>Any Crash files</li>
    <li>Any NTP Issues</li>
    <li>Dbreplication status</li>
    <li>Cluster Network status - Road Mapped</li>
    <li>Network Status</li>
    <li>Upgrade status</li>
</ol>
