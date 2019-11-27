# health.py
Basic script that logs into CUCM using paramiko and pull down health check information. Writes results to text file.
Idea to do pre upgrade checks and maintains copy of results for anayalsis before upgrade and for reference post upgrade.

## 
The program will ask for os username and password of nodes in a cluster and run Health Checks on them.
    1.Pre 8.0 mode enabled
    2.Cluster securitu mode enable
    3.ITL Errors
    4.CTL Errors
    6.Backup History
    7.Any Crash files
    8.Any NTP Issues
    9.Dbreplication status
    10.Cluster Network status - Road Mapped
    11.Genernal Status
    12.Network Status
    13.Upgrade status


