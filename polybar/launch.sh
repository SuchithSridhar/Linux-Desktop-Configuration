#!/usr/bin/env sh

# More info : https://github.com/jaagr/polybar/wiki

# Install the following applications for polybar and icons in polybar if you are on ArcoLinuxD
# awesome-terminal-fonts
# Tip : There are other interesting fonts that provide icons like nerd-fonts-complete
# --log=error
# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar > /dev/null; do sleep 1; done

count=$(xrandr --query | grep " connected" | cut -d" " -f1 | wc -l)

case $count in
    "1")
        primary='eDP'
        ;;
    "2")
        primary='HDMI-A-0'
        ;;
    "3")
        primary='HDMI-A-0'
        ;;
    *)
        primary='eDP'
        ;;
esac

MONITOR=$primary polybar --reload mainbar-i3 -c ~/.config/polybar/config.ini &

sleep 1

for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    if [ "$m" != "$primary" ]; then
        MONITOR=$m polybar --reload mainbar-i3 -c ~/.config/polybar/config.ini &
    fi
done
