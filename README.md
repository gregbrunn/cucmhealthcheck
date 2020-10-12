# health.py
<p>Basic script that logs into CUCM using paramiko and pull down health check information. Writes results to text file.
Idea to do pre upgrade checks and maintains copy of results for anayalsis before upgrade and for reference post upgrade.</p>

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
