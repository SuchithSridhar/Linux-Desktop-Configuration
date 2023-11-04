#!/bin/sh

# Must run pacman -Sy as root in the background to actually update
# packages
yay -Qu | wc -l
