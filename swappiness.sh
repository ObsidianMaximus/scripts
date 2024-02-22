#!/usr/bin/bash


cat /proc/sys/vm/swappiness

echo "# Reduce the inclination to swap
vm.swappiness=20" | sudo tee -a /etc/sysctl.conf
