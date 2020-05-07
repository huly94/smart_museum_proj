# Project Smart Museum: introduction

museums are one of the most important cultural destinations for tourists and non. Indeed, they contains a collection of 
works linked to one or more cultural aspect like art, science or technology. Today, museums are diffused in all the cities 
of the world, and their main task is not only to preserve objects and works of art, but also spread knowledge through 
the organization of exhibitions, guided tours and conferences. In order to do this, museums looks for increasingly 
involving experiences, suitable for all the ages. This is right the purpose of this project. To do this, 
we have to set a smart environment, composed by sensors, applications and actuators, seen as transducers, 
automatized by an overall entity, called orchestrator. In the next paragraphs we want to show our approach, 
providing also some examples, the physical and software composition of sensors and actuators, a description 
of the applications we have chosen and an overview on the orchestrator tasks.

## 1.1 THE APPROACH

The main challenge is to design an environment in which the experience provided is customized, in order to satisfy the need of everyone. In particular one of the principal feature is to make a distinction on the age of the visitor, in order that the information provided are filtered by age. The project is based on the python library python-statemachine (https://pypi.org/project/python-statemachine/) that we used to represent sensors, actuators and processes, or applications, as state machine. We first have to provide a definition of these objects:
1. Sensors: represent a physical sensor that can be placed inside a museum to get certain inputs.
2. Actuators: Represents a physical device that produce a certain output
3. Applications (Processes): An application models a certain use case that we have inside a museum. An example of application is the managing of the light basing on time, weather or visitor presence, or the reproduction of an audio track related to a work, basing on the age of the visitor.

So the applications are state machines that are triggered by the activation of a sensor, thanks to which we have a 
transition in another state in which the application can make use of an actuator to reach its goal (switch on the light, 
play an audio track and so on). To achieve this situation we need intermediary between sensor and apps, able to recognize 
the signal sent by the sensor and create the correct application and actuator to associate. this is possible thanks 
to a register, that the orchestrator has, that is composed by two maps: one has a sensor as key and as value the list 
of app associated, the other one has an application as key and as value the list of actuators related. 
In the following interaction diagram we describe how the interaction between objects take place:

![Image description](https://i.ibb.co/mcFSsCB/sequence.png)

Of course, the activation of the sensor is due to the activation of the physical sensor, and at the activation of the 
software object of the actuator correspond the activation of the physical actuator. We choose this approach because 
automatize the overall process, allowing to the orchestrator to decide which app should be activated basing on the inputs
received. So we can consider the various state machines as transducers, that convert a signal into another one, and the 
orchestrator as a multiplexer.

## 1.2 THE ARCHITECTURE 

We can consider the overall system as as an event-driven architecture, in which the principal aim is the  production, 
detection, consumption of, and reaction to events. 

![EDA architechture](https://www.researchgate.net/profile/Joao_Barraca/publication/259753992/figure/fig7/AS:667934183657498@1536259327412/Conceptual-Architecture-of-a-Smart-Environment.png)

In our case the sensors placed in the museum are the event emitter, that  have the responsibility to detect, gather, 
and transfer events. Actuators instead are the event consumers, that have the responsibility of applying a reaction as 
soon as an event is presented. The central part of management and reasoning is entrusted to the orchestrator. So the final 
architecture is the following:

![EDA_proj](https://i.ibb.co/2k0J21m/Eda-architecture.png)

Instead the software architecture is the following:

![EDA_proj](https://i.ibb.co/tHVG3gM/UML.png)

Where the applications are observers while the orchestrator is a singleton

## 1.3 SENSORS AND ACTUATORS

Sensors and actuators refer to real sensors and actuators, and for this reason here we provide a description of sensors 
and actuators used:
1. Sensors:
   - **Sensor visitor age**:  We need this sensor to distinguish different ages of visitors, in order to play to them different 
   audio tracks and also to give them different experiences. Therefore the right solution is the RFID thanks to which we can transmit 
   information about the age of a visitor through a tag attached for example on the audio guide provided at the beginning of the visit.
   An example can be a RFID reader, with functionality read only, that detects tags at a distance of max 5 meters  
   ![RFID_reader](https://i.ibb.co/5KQ3MXt/RFID-Illustration.png)
   - SensorTimer: This sensor is triggered at the expiration of a simple timer. We need it in order to provide further 
   information about a work if the visitor, at the end of the track, wants to know more about that particular work.
  
   - **SensorClock**: A sensor based on the clock. We need it to know the time, in order to turn the lights when it’s dark.
     Both SensorTimer and SensorClock can be realized using a system call 
    
   - **SensorWeather**: A sensor that detects the weather, in order to turn the lights on when there are clouds. 
     It can be a portable cloud sensor. The Portable Cloud Sensor measures the amount of cloud cover by comparing the 
     temperature of the sky to the ambient ground level temperature. The sky temperature is determined by measuring the 
     amount of radiation in the 8 to 14 micron infrared band. A large difference indicates clear skies, whereas a small
     difference indicates dense, low-level clouds. This allows the sensor to continuously monitor the clarity of the 
     skies, and to alert the user when conditions change. A built-in daylight sensor is also included. When the sensor 
     is set to detect “Clear & Dark” conditions, it will alarm for clear skies. When the sensor is set to detect 
     “Cloudy or Light” conditions, it will alert you when clouds roll in or dawn approaches
     ![cloud_sensor](https://diffractionlimited.com/wp-content/uploads/2016/08/Img_5834.jpg)
     
     Another solution can be using a web service that give continuously the weather. There are several weather APIs, an example 
     can be OpenWeatherMap
   - **SensorPresence**: a simple occupancy sensor (probably a passive infraRed sensor) that detects if there is at least 
     one visitor in the area or none. We need this sensor for the light managing. It is an electronic sensor that 
     measures infrared (IR) light radiating from objects in its field of view.
    ![prensence_sensor](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Light_switch_with_passive_infrared_sensor.jpg/150px-Light_switch_with_passive_infrared_sensor.jpg)
   
   - **SensorMobile**: This sensor is triggered by the pushing on a button (placed or in a mobile application or on the audio guide itself), 
     when a visitor need suggestions on works related to the one is currently watching, in this case a colored light
     guide him on other works. 
   
   - **SensorColor and SensorGesture**: These two sensors are related to the pervasive game “chromatize it!” in which a 
     visitor using a device takes a color (in the form of a light source) and uses it to color a wall. So the sensor 
     color has to detect the color coming out from that light source, and the sensor gesture it’s a motion sensor that 
     detect when a visitor pass the paint on the smart wall. the sensor color can be a sparkFun RGB light sensor - ISL29125.
     The ISL29125 breakout board makes it very easy to sense and record the light intensity of the general red, green,
     and blue spectrums of visible light while rejecting IR from light sources.
    ![color_sensor](https://cdn.sparkfun.com//assets/parts/9/6/7/7/12829-01.jpg)

2. Actuators:
   
   - **ActuatorAudio**: it is the headphones plugged to the visitor audio-guide, that turn on when visitor stand in front 
     of a work, playing a certain audio track basing on the age. So the audio-guide has the tag that is detected by the 
     RFID reader. examples can be the following:
     ![audio-guide_RFID](https://sc01.alicdn.com/kf/HTB1ZRmKtyOYBuNjSsD4q6zSkFXaa.jpg)
   - **ActuatorLight**: these are the lights inside the room that turn on or off basing on time, weather and presence of a 
     visitor.
   - **ActuatorMobile**: In this case the actuator can be a mobile or any device to which we can send message like 
     suggestions on related exhibitions or works, so even the audio-guide itself can be a good actuator.
   - **ActuatorWall**: this is the smart wall that is colored during the pervasive game ”chromatize it!”
    ![smart_wall](https://i.ibb.co/rMCM5kM/Schermata-2020-05-07-alle-10-55-07.png)
   - **ActuatorPainting**: a painting itself can be an actuator, this only in cases of animated works that can be based 
     on what the visitor like most in an exhibition. It can be just a screen that basing on the visitor show different
     things.

The code of sensors and actuators is very similar, indeed both implements a two-state machine, with the only difference
that the sensor has a notify method when it is activated. These are examples of code for sensors and actuators:
![code_sensor](https://i.ibb.co/VJGbTVb/Schermata-2020-05-07-alle-11-15-40.png)

![code_actuator](https://i.ibb.co/qrQ2051/Schermata-2020-05-07-alle-11-17-12.png)

## 1.4 APPLICATIONS

Applications model a certain use case that we can have inside the museum. We can have two types of applications: 
a general application, that takes care of an overall task like the managing of the light, and a dedicated application 
that depends from the visitor. Indeed different visitors can be in different states of the same application, for example 
a visitor that is just arrived at a work cannot be in the same state of a visitor that is in front of it since several 
minutes. In the following images we represent all the applications implemented in this project, through a state diagram:


