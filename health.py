#! python3
#The following is used to ssh into all nodes in a cluster at once and pull dbreplication status
#Need to add multithreading.

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



# This function uploads the .wav file to all MoH servers defined in the pub_sub_ip_list
def login(server_ip, os_user, os_pass):
    output=[]
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #print('server_ip:',server_ip)
    ssh.connect(server_ip, username=os_user, password=os_pass)
    interact = SSHClientInteraction(ssh, timeout=90, display=True)

    # "display=True" is just to show you what script does in real time. While in production you can set it to False
    interact.expect('admin:')
    interact.send("run sql select paramname,paramvalue from processconfig where paramname='RollBackToPreGrayback'")
    interact.expect('admin:')
    output.append(interact.current_output)
    interact.send("run sql select paramname,paramvalue from processconfig where paramname='ClusterSecurityMode'")
    interact.expect('admin:')
    output.append(interact.current_output)
    interact.send("show itl")
    interact.expect('admin:')
    output.append(interact.current_output)              
    interact.send("show ctl")
    interact.expect('admin:')
    output.append(interact.current_output) 
    #interact.send("file view install system-history.log")
    #interact.expect('admin:')
    interact.send("utils disaster_recovery history backup")
    interact.expect('admin:')
    output.append(interact.current_output) 
    interact.send("utils service list")
    interact.expect('admin:')
    output.append(interact.current_output) 
    #interact.send("utils network connectivity",) #Need to come back here this comman is not what I thought will want to run to each node.
    #interact.expect(['admin:', 'Continue (y/n)?'])
    #if interact.last_match == 'Continue (y/n)?':
    #        interact.send('y')
    #        interact.expect('admin:')
    #interact.expect("This command can take up to 3 minutes to complete.\nContinue (y/n)?")
    #interact.send("y")
    #interact.expect('admin:')    
    interact.send("utils core active list")
    interact.expect('admin:')
    output.append(interact.current_output) 
    interact.send("utils ntp status")
    interact.expect('admin:')
    output.append(interact.current_output) 
    interact.send("utils dbreplication runtimestate")
    interact.expect('admin:')
    output.append(interact.current_output) 
    interact.send("show network cluster")
    interact.expect('admin:')
    output.append(interact.current_output) 
    interact.send("show status")
    interact.expect('admin:')
    output.append(interact.current_output) 
    interact.send("utils diagnose test")
    interact.expect('admin:')
    output.append(interact.current_output)
    interact.send("utils system upgrade status")
    interact.expect('admin:')
    output.append(interact.current_output)
    ssh.close()
    ip_file_name = server_ip.replace('.', '_')
    ip_file_name2 ="Health_Check_"+ip_file_name
    output_file = '{}.txt'.format(ip_file_name2)
    with open(output_file, 'w') as out:
        for command in output:
            out.write("%s\n" % command)


    
def main():
    print('='*80)
    print(" _   _            _ _   _      ")
    print("| | | | ___  __ _| | |_| |__   ")
    print("| |_| |/ _ \/ _` | | __| '_ \  ")
    print("|  _  |  __/ (_| | | |_| | | | ")
    print("|_| |_|\___|\__,_|_|\__|_| |_| ")                
    print("  ____ _               _    ")
    print(" / ___| |__   ___  ___| | __ ")
    print("| |   | '_ \ / _ \/ __| |/ / ")
    print("| |___| | | |  __/ (__|   <  ")
    print(" \____|_| |_|\___|\___|_|\_\ ")
    print('='*80)
    print('The following program will ask for os username and password \nof nodes in a cluster and run Health Checks on them')
    print('1.Pre 8.0 mode enabled')
    print('2.Cluster securitu mode enable')
    print('3.ITL Error')
    print('4.CTL Error')
    print('5.System History- Road Mapped') #removed for now
    print('6.Backup History')
    print('7.Any Crash file present')
    print('8.Any NTP Issues')
    print('9.Dbreplication status')
    print('10.Cluster Network status - Road Mapped')
    print('11.Genernal Status')
    print('12.Network Status')
    print('13.Upgrade status')
                   
#Loop to enter IP address of nodes.
    i=0
    list_of_nodes_ipaddr=[]
    while True:
        print('When Finished Type END')
        print('Enter the IP address of Node'+str(i)+':')
        ipaddr= input()
        i+=1
        if ipaddr=='END':
              break
        list_of_nodes_ipaddr=list_of_nodes_ipaddr +[ipaddr]
    i=0
#prints the IP address you entered
    for i in range(len(list_of_nodes_ipaddr)):
        print('Node' + str(i) + ': ' + list_of_nodes_ipaddr[i])
        i+=1
    
    os_user=input('Enter SSH or Platform Username:')
    os_pass=getpass.getpass(prompt='Enter SSH or Platform password:')
    start_time = time.time() 
    print('Start time:',start_time)
    print(str(start_time))
    print('Programing running ....')
    i=0
    #Here is where I need to start on threading
    for i in range(len(list_of_nodes_ipaddr)):
        t = threading.Thread(target = login, args = (list_of_nodes_ipaddr[i],os_user,os_pass))   # as an example, on the first iteration "i[0]" equals to "connection[0][0]" which equals to IP address 10.10.10.10
        t.daemon = True
        t.start()
        i+=1
 


         
if __name__ =='__main__':
    main()
