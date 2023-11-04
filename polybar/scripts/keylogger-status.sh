#/bin/bash
# Author: Suchith Sridhar
# Website: https://suchicodes.com/
#
# This is the script used by polybar to show the icon
# that corresponds to the current keylogger state.

SCRIPT="[b]in/custom-scripts/keylogger.py"
OUTPUT=$(pgrep -af "$SCRIPT" | cut -d" " -f1)
if [ -z "$OUTPUT" ]; then
    echo ""
else
    echo ""
fi
