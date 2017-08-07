# This file should be run on system boot.

#sudo mount -o remount,rw /
#exit

#sudo raspivid -t 1000000
#sudo shutdown -h 0

sudo mount /dev/sda /mnt
sudo python /home/pi/camera.py
sleep 15
sudo reboot
