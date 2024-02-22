#!/usr/bin/bash

sudo mkdir -v /etc/systemd/system/fstrim.timer.d
sudo touch /etc/systemd/system/fstrim.timer.d/override.conf
echo "[Timer]
OnCalendar=
OnCalendar=daily" | sudo tee -a /etc/systemd/system/fstrim.timer.d/override.conf
