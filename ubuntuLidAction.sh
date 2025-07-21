#!/bin/bash

LOGIN_CONFIG_FILE="/etc/systemd/logind.conf"
LID_SWITCH_BATTERY="HandleLidSwitch=suspend"
LID_SWITCH_AC="HandleLidSwitchExternalPower=ignore"

if [ "$(id -u)" -ne 0 ]; then
  echo "This script must be run as root. Please use sudo." >&2
  exit 1
fi

if [ ! -f "$LOGIN_CONFIG_FILE" ]; then
    echo "Error: Configuration file not found at $LOGIN_CONFIG_FILE" >&2
    exit 1
fi

echo "Configuring lid close actions in $LOGIN_CONFIG_FILE..."

if grep -q "^#*HandleLidSwitch=" "$LOGIN_CONFIG_FILE"; then
    sed -i "s/^#*HandleLidSwitch=.*/$LID_SWITCH_BATTERY/" "$LOGIN_CONFIG_FILE"
    echo "Updated: $LID_SWITCH_BATTERY"
else
    echo "$LID_SWITCH_BATTERY" >> "$LOGIN_CONFIG_FILE"
    echo "Added: $LID_SWITCH_BATTERY"
fi

if grep -q "^#*HandleLidSwitchExternalPower=" "$LOGIN_CONFIG_FILE"; then
    sed -i "s/^#*HandleLidSwitchExternalPower=.*/$LID_SWITCH_AC/" "$LOGIN_CONFIG_FILE"
    echo "Updated: $LID_SWITCH_AC"
else
    echo "$LID_SWITCH_AC" >> "$LOGIN_CONFIG_FILE"
    echo "Added: $LID_SWITCH_AC"
fi

echo "Restarting systemd-logind service to apply changes..."
if systemctl restart systemd-logind.service; then
    echo "Configuration successfully applied!"
else
    echo "Error: Failed to restart systemd-logind.service." >&2
    exit 1
fi

exit 0
