# Project Smart Museum
The aim of this project is to create a smart environment inside a museum, in order to give a more involved experience, suitable for everyone.
In particular we want to represent its processes and objects as transducers. The problem of automatize the overall process
with the introduction an orchestrator function that dynamically assign objects to processes.

the project is based on the python library python-statemachine [https://pypi.org/project/python-statemachine/] that we use 
to realize objects and processes that compose it.

Objects are sensor and actuators. Sensors used in this projects are motion sensor, to detect the arrival of a visitor,
sensors based on time and a timer expiration, sensor for mobile detection and sensors that detect the weather. 
Also with the introduction of pervasive games we add a sensor for color detection and for gesture detection. 
Actuators, instead are audio, to reproduce a certain track related to a work, lights, to manage a work or a room 
illumination, mobile, to send messages to a visitor or also a work actuator in the case of interactive works. also with
the introduction of the pervasive game we add the painting and wall actuator. In particular, since one of the feature of
this project is to assign a different audio track basing on the age of the visitor, so an example of a possible physical 
implementation of this sensor can be by using a device that is provided at the beginning of the visit to each visitor. This device 
communicate with sensors with RFID that contains informations about the user. Also to this device are connected headphones
that are the actuator on wich reproduce the audio track

Processes are the application (app) of my project. they model a certain use case that we can have inside a museum. One 
example is the app linked to the managing of the lights that can switch on or off basing on the presence of a visitor, 
basing on the weather conditions or basing on time condition(day or night). 
Below we have the description of each app and its state machine diagram:



![State machines diagram1](https://i.ibb.co/qk4tsm5/State-machines-diagrams-1.png)
![State machines diagram2](https://i.ibb.co/NSRbLPW/State-machines-diagrams-2.png)
![State machines diagram3](https://i.ibb.co/Jx174Rp/State-machines-diagrams-3.png)
![State machines diagram4](https://i.ibb.co/NYKX54k/State-machines-diagrams-4.png)




