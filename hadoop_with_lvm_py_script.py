import os
import getpass

os.system("tput setaf 3")
print("\t\t\tJust Press and get things done!!")
os.system("tput setaf 7")
print("\t\t\t---------------------------------------")


passwd = getpass.getpass("Enter password:")
if passwd!="lvm":
    print("password incorrect")
    exit()

while True:
    os.system("clear")
    print("""
    \n
    Press 1 : To check how many storage is attached to the OS
    Press 2 : To create Physical Volume
    Press 3 : To display Physical Volume
    Press 4 : To create Volume Group
    Press 5 : To display Volume Group
    Press 6 : To create Logical Volume
    Press 7 : To display Logical Volume
    Press 8 : To format the LV
    Press 9 : To Exit
    """)

    ch = input("Enter your Choice:")
    print(ch)

    if int(ch)==1:
        os.system("fdisk -l")

    elif int(ch)==2:
        pv1=input("Enter the name of storage 1:")
        pv2=input("Enter the name of storage 2:")
        os.system("pvcreate {}".format(pv1))
        os.system("pvcreate {}".format(pv2))

    elif int(ch)==3:
        pv=input("Enter the name of storage:")
        os.system("pvdisplay {}".format(pv))
        
    elif int(ch)==4:
        vgn=input("Give name to the VG:")
        pvn1=input("Enter the name of storage 1:")
        pvn2=input("Enter the name of Storage 2:")
        os.system("vgcreate {} {} {}".format(vgn,pvn1,pvn2))

    elif int(ch)==5:
        vgn1=input("Enter the name of VG:")
        os.sytem("vgdisplay {}".format(vgn1))

    elif int(ch)==6:
        size=input("Enter size for your LV:")
        lvn=input("Give name to your LV:")
        vgn2=input("Enter name of the VG:")
        os.system("lvcreate --size{} --name{} {}".format(size,lvn,vgn2))
                         
    elif int(ch)==7:
        os.system("lvdisplay")

    elif int(ch)==8:
        vgn4=input("Enter the name of VG:")
        lvn2=input("Enter the name of LV:")
        os.system("mkfs.ext4  /dev{}{}".format(vgn4,lvn2))

    elif int(ch)==9:
        exit()

    else:
        print("Not Supported")

    input("\nPlease enter to continue...")