#!/bin/sh

# Script to modify screen brightness using xrandr.

echo -n "Enter a brightness value (1-10) : "

read LEVEL

case $LEVEL in
	1)
		xrandr --output eDP-1 --brightness 0.1
		;;
	2)
		xrandr --output eDP-1 --brightness 0.2
		;;
	3)
		xrandr --output eDP-1 --brightness 0.3
		;;
	4)
		xrandr --output eDP-1 --brightness 0.4
		;;
	5)
		xrandr --output eDP-1 --brightness 0.5
		;;
	6)
		xrandr --output eDP-1 --brightness 0.6
		;;
	7)
		xrandr --output eDP-1 --brightness 0.7
		;;
	8)
		xrandr --output eDP-1 --brightness 0.8
		;;
	9)
		xrandr --output eDP-1 --brightness 0.9
		;;
	10)
		xrandr --output eDP-1 --brightness 1
		;;
	*)
		echo -n "Wrong input value range! Please select between 1 and 10!"
		;;
esac
