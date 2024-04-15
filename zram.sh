#!/bin/bash

# Installing zram-generator and editing its contents
sudo apt install systemd-zram-generator #&& sudo nvim /etc/systemd/zram-generator.conf


echo "[zram0] 
compression-algorithm = zstd
zram-fraction = 1 # zram-size does not work anymore, so have this line instead.
max-zram-size = 100000 # this has been done because by default, the script takes 4gb as max zram size, thus had to override it." | sudo tee /etc/systemd/zram-generator.conf

 

#Then run this - 

sudo systemctl start /dev/zram0


#Finally execute this command - 

echo "# Increase the inclination to swap to zram
vm.swappiness=100" | sudo tee -a /etc/sysctl.conf


# Once all this is done, reboot your computer and enter :
#zramctl 
