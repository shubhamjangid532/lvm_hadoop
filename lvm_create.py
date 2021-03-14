#!/usr/bin/python3
import subprocess as sp
import getpass as gp

ip_dn = input("Enter The IP of system Which you want to make the data node:- ")
ip_nn = input("Enter The IP of system Which you want to make the name node:- ")

p_dn = gp.getpass("Enter the passwd of Data Node :- ")
p_nn = gp.getpass("Enter the passwd of Name Node :- ")

print("This is compulsury To add the both of HDD with the Name node")


hdd1 = input("Enter the first HHD name Which you want to add in VG :- ")
hdd2 = input("Enter the second HHD name Which you want to add in VG :- ")

create_pv1 = "sshpass -p " + p_dn + " ssh root@" + ip_dn + " pvcreate " + hdd1
create_pv2 = "sshpass -p " + p_dn + "  ssh root@" + ip_dn + " pvcreate " + hdd2
create_vg = "sshpass -p " + p_dn + " ssh root@" + ip_dn + " vgcreate dynamic_storage " + hdd1 + " " + hdd2

create_lv = "sshpass -p " + p_dn + "  ssh root@" + ip_dn + " lvcreate --size 12G --name hadoop_dn dynamic_storage"
format_lv = "sshpass -p " + p_dn + " ssh root@" + ip_dn + " mkfs.ext4 /dev/dynamic_storage/hadoop_dn"

create_dir = "sshpass -p " + p_dn + " ssh root@" + ip_dn + " mkdir /datanode"
mnt_dir = "sshpass -p " + p_dn + " ssh root@" + ip_dn + "  mount /dev/dynamic_storage/hadoop_dn /data_node/"
show_mnt = "sshpass -p " + p_dn + " ssh root@" + ip_dn + "  df -h"

sp.getoutput(create_pv1)
sp.getoutput(create_pv2)
sp.getoutput(create_vg)
sp.getoutput(create_lv)
sp.getoutput(format_lv)
sp.getoutput(create_dir)
sp.getoutput(mnt_dir)
sp.getoutput(show_mnt)



