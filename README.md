# BIOE421_RoboHand Final Project 

### Robo-Testing Hand
### Michaela Dimoff & Paul Greenfield
### Team02_TeamGuinness
## Brainstorming

Our microcontrollers applications project will be directed at developing an device that simulates the movement of a residual limb of a child with symbrachydactyly. This device will be used to help test prosthetic hands that are being developed to help children with this condition. The artificial residual limb will have a range of motion of at least 60 degrees in one direction that simulates flexion and extension of the wrist. The project will utilize a GUI to accept varying user inputs of desired flexion or extension degrees. The user will be able to control the artificial limb position with a precision of 10 degrees, as well as selecting the speed and number of repetitions of flexion and extension that the limb performs. 

__Use Cases:__
* Change the position of the arm
* Change the number of repetitions 
* Changing the speed
* Changing the diameter of the residual limb
* Changing the direction of motion from extension/flexion to ulnar/radial deviation
	* This is currently outside of the scope but would be cool to keep in mind for the future

## Abstract

Due to children’s fast growth rates, low cost is a necessity for families when considering prosthetics for a child. Prosthetic hands developed by the “e-Nableing the Future” group can be 3D printed and assembled by anyone with access to the internet, a 3D printer, and basic tools. However, e-Nable prosthetics have significant limitations, including low force-translation efficiency and a limited range of motion. Furthermore, no device exists that can be used to quantitatively evaluate prototypes of e-Nable prosthetics; Team Guinness seeks to fill that gap. We plan to use Python v.3 on a Raspberry Pi to develop a graphical user interface (GUI) that takes user input for the desired degree of flexion or extension of an artificial wrist-palm device, along with the number of repetitions of the motion. The GUI will convert these user inputs into a Gcode file that will be automatically sent through Pronterface to a RAMBo. The RAMBo, supported by Marlin firmware, will turn an Ultimachine stepper motor that is connected to an artificial wrist-and-palm setup via a pulley system. The rotation of the motor causes the palm to rotate about the wrist in the arc specified by the user in the GUI. Further development of the device, such as attaching an e-Nable prosthetic to the wrist-palm device, adding force sensors, and adding additional degrees of freedom, will allow for analysis of ulnar/radial deviation or pronation/supination. These advances will allow for a more quantitative measurement of the force required to use the e-Nable prosthetics and will be undertaken by the Carpal Diem senior design team.

