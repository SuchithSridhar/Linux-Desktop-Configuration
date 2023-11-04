#/bin/bash
# Author: Suchith Sridhar
# Website: https://suchicodes.com/
#
# This is the script used by polybar to show the icon
# that corresponds to the current keylogger state.

SCRIPT=".local/bin/custom-scripts/keylogger.py"
if ( pgrep -af "$SCRIPT" > /dev/null ); then
    echo ""
else
    echo ""
fi
