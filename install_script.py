import os
import time
import sys
import subprocess

os.system("sudo apt update && sudo apt install curl -y")

def purge_ff():
    '''This function removes firefox entirely from the user system'''
    ff_rm = input("\nDo you REALLY wish to remove firefox entirely from your system? [y/n] ")

    if ff_rm.lower() == "y":
        os.system("sudo apt purge firefox* && rm -rf ~/.mozilla && sudo rm -rf /etc/firefox*")
        if(os.path.isdir("/usr/lib/firefox")):
            os.system("sudo rm -rf /usr/lib/firefox")
        if(os.path.isdir("/usr/lib/firefox-addons")):
            os.system("sudo rm -rf /usr/lib/firefox-addons")
        print("\nFirefox has been succesfully removed from your system!")
    else:
        print("\nAbort")

def purge_thunder():
    '''This function fully removes thunderbird email client'''
    tb_rm = input("\nDo you REALLY wish to remove thunderbird entirely from your system? [y/n] ")

    if tb_rm.lower() == "y":
        os.system("sudo apt purge thunderbird*")
        if(os.path.isdir("~/.thunderbird")):
            os.system("rm -rf ~/.thunderbird")
        print("\nThunderbird has been succesfully removed from your system!")
    else:
        print("\nAbort")

def trim():
    '''This function enables TRIM on devices that have a SSD that supports it.'''
    os.system("curl -O https://raw.githubusercontent.com/ObsidianMaximus/scripts/master/trim.sh && chmod +x trim.sh")
    subprocess.run(["./trim.sh"])
    os.system("rm trim.sh")

    # Now, we will reduce the swappiness value, so that the kernel uses the swapfile/swap partition less frequently, thus preserving the SSD lifespan.    
    reduce_swap = subprocess.run(['cat', '/proc/sys/vm/swappiness'], stdout=subprocess.PIPE)
    if reduce_swap.stdout.decode(encoding='UTF-8')!=20:
        os.system('echo "vm.swappiness=20" | sudo tee -a /etc/sysctl.conf')
        print("\nTRIM set up for running daily! [Along with reducing the inclination to swap.]")
    else:
        print("\nTRIM set up for running daily!")


def brave():
    '''This function installs brave browser'''

    os.system("curl -O https://raw.githubusercontent.com/ObsidianMaximus/scripts/master/brave.sh && chmod +x brave.sh")
    subprocess.run(["./brave.sh"])
    os.system("rm brave.sh")
    print("\nInstalled the brave browser successfully!")

def wifi_drivers():
    '''This function installs the wifi drivers for TP Link Archer T2U Plus [which uses rtl8812au]'''
    install_drivers = input("\nDo you have a TP Link Archer T2U Plus [rtl8812au]? If yes, do you want to install the necessary drivers for it? [y/n] ")

    if install_drivers.lower() == "y":
        os.system("curl -O https://raw.githubusercontent.com/ObsidianMaximus/wifidrivers/master/commands_for_drivers.sh && chmod +x commands_for_drivers.sh && bash commands_for_drivers.sh && rm commands_for_drivers.sh")
        print("\nSuccessfully installed the wifi drivers!")
    else:
        print("Abort")

def zram_install():
    '''This function removes swapfile and installs ZRAM'''

    yes_no = input("Do you wish to install ZRAM on your device? [y/n] ")

    if yes_no.lower() == 'y':
        print("\nProcedding to install ZRAM...")
        os.system("curl -O https://raw.githubusercontent.com/ObsidianMaximus/scripts/master/zram.sh && chmod +x zram.sh")
        z_ratio = float(input("\nEnter the ZRAM ratio to set (This ratio is the ratio to your physical RAM, for eg 1 will mean allot same amount of ZRAM as the size of the physical ram): "))
        
        if z_ratio <= 0:
            print("\nInvalid ratio entered, setting default ZRAM ratio to 2 [edit this ratio in \'/etc/systemd/zram-generator.conf\']")
            subprocess.run(["./zram.sh 2"])
        else:
            print(f"\nSetting the ZRAM ratio to {z_ratio}\n")
            subprocess.run(["./zram.sh", str(z_ratio)])
            print("\nSuccessfully configured ZRAM on your device, please reboot to allow the changes to take effect.")
    else:
        print("\nAbort")


def main():
    '''This is the main function'''
    purge_ff()

    purge_thunder()

    trim_var = input("\nIf you have an SSD, you should enable TRIM to trim the ssd and improve it's lifespan. Enable TRIM? [y/n] ")
    if trim_var.lower() == "y":
        trim()
    else:
        print("\nAbort")

    brave_var = input("\nDo you wish to install brave browser? [y/n] ")
    if brave_var == "y":
        brave()
    else:
        print("\nAbort")

    wifi_drivers()

    zram_install()

if __name__ == "__main__":

    main()
