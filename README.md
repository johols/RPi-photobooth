# RPi-photobooth
Camera and photo printer controlled by a raspberry pi. This project is based on the instructions from this post: http://www.instructables.com/id/Raspberry-Pi-photo-booth-controller



Front | BAck
------------ | -------------
![GitHub Logo](/photobooth_front.png) | ![GitHub Logo](/photobooth_back.jpg)
Circuit | Description
![GitHub Logo](/circuit.png) | 1K ohm, 10K ohm, 330 ohm, 4 leds, push switch

##Setup
Follow instructions from link. 
Printer: Canon SELPHY 910
Camera: Canon
Raspberry Pi 2

###Set Raspberry to startup script on reboot
`sudo nano /etc/rc.local`

##Note
- one extra button (with built-in led) is added. It is used to restart the main python script (button.py) when the script accidently stops. This typically happens when the camera goes into sleep mode. This second button is controlled by the script restart_button.py. 
- after a successfull print, the system is set to reboot. This is because sometimes the printer goes into paus mode (hangs). It might not be necessary if you change error policy. See: https://lwn.net/Articles/498216/  or  https://bbs.archlinux.org/viewtopic.php?id=202022  or   https://www.novell.com/support/kb/doc.php?id=7014022

##TODO
- add externas USB disk or flash memory to store the pictuers before removing them.


##Useful commands
Sometimes printer hangs (out of paper, for example): Printer Canon_CP910 disabled since Tue 17 May 2016 21:26:12 UTC -
	Unable to send data to printer.

`cupsenable Canon_CP910`

List printer name

`lpstat -p`

List all printer jobs

`lpstat -o`

Printer status

`lpc status`

To find the Raspberry Pi IP on your network (check this output for items that are not incomplete, then make 'ssh pi@192.168.0.XX')

`ifconfig | grep broadcast | arp -a`
