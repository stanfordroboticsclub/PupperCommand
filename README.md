# PupperCommand
## Installation
```shell
sudo bash install.sh
```
## Starting the joystick publisher
1. Put the PS4 controller into pairing mode by holding the share and PS button at the same time. The light should start blinking in bursts of two. 
2. Run script
```shell
sudo systemctl start joystick
sudo python3 joystick.py &
```

## Debugging 
To see if the controller is publishing to the Rover topic use: 
```shell
rover peek 8830
```
