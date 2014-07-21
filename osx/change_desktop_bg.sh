#! /bin/bash
 #script to change all desktop backgrounds
echo -n "Drag and drop an image file here then press ‘return’ or press ‘control-c’ to cancel…"
read -e WLPR;
function change_wallpaper
 {
 defaults write com.apple.desktop Background "{default = { ImageFilePath='$WLPR'; };}"; killall Dock
 }
 change_wallpaper