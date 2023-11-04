#/bin/bash
# Author: Suchith Sridhar
# Website: https://suchicodes.com/
#
# This is the script used by polybar to show the icon
# that corresponds to the current mic state.

if ( amixer | grep "Capture" | grep -q "off" ); then
    echo ""
else
    echo ""
fi
