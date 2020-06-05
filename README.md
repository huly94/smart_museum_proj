# Project Smart Museum: introduction

museums are one of the most important cultural destinations for tourists and not. Indeed, they contain a collection of 
works linked to one or more cultural aspect like art, science or technology. Today, museums are diffused in all the cities 
of the world, and their main task is not only to preserve objects and works of art, but also spread knowledge through 
the organization of exhibitions, guided tours and conferences. However, with the technological progress, museums need to
modernize themselves. So, museums have some needs that can be satisfied using IoT, that permits to introduce increasingly 
involving and more interactive experiences suitable for all the ages. Also, even smart environments, and in particular smart museums, have some needs: first a set of devices, sensors and actuators, that permit to interact with users. These elements don't have a one-way approach, one device indeed can be used for multiple purposes. Then to bring all these devices together, is important to create a network, Wi-Fi for example. We can have more than one network where devices are connected (Bluetooth, ethernet and so on). There is also the need for a component that analyzes and processes sensed data for the extraction of knowledge, events and high-level information. 
This is right the purpose of this project. To do this, 
we have to set a smart environment, composed by sensors, applications and actuators, seen as transducers, 
automatized by an overall entity, called orchestrator.

In the next paragraphs, we want to show our approach, 
providing also some examples, the physical and software composition of sensors and actuators, a description 
of the applications we have chosen and an overview on the orchestrator tasks.

## 1.1 THE APPROACH

The project is realized with the python library 
python-statemachine (https://pypi.org/project/python-statemachine/), used to represent sensors, actuators and processes, 
or applications, as a state machine. We first have to define these objects:

1. Sensors: represent a physical sensor that can be placed inside a museum to get certain inputs.
2. Actuators: Represents a physical device that produce a certain output
3. Applications (Processes): An application models a specific use case, a specific scenario, that we have inside a museum. An example of application is the managing of the light basing on time, weather or visitor presence, or the reproduction of an audio track related to a work, based on the age of the visitor.

The main challenge is to design an environment in which the experience provided is customized, to satisfy the need of everyone. One of the first targets is to make the configuration of the environment generic. In this way, we can install the applications we need, specifying properties of interest, like area or typology. These two properties are fundamentals in our environment:
 
- We have the division of a room in different **areas**, to specify for an application the area to which belongs. Also, in the virtual reproduction of the room, we set the area of the sensor
- **Typology** is a more complex concept. First, we can distinguish between individual and general applications. For individual tasks, like the reproduction of a track for a visitor, we have individual applications, while, for general tasks, like the light managing, we have general applications. This distinction arises from the fact that different visitors can be in different states of the same application, so we need two different instances of the same app for each of them, while, for general application, is enough to have only one instance.

So, we have a division of the museum in areas and a distinction of the applications in typologies. Applications are state machines that are triggered by the activation of a sensor. The latter makes possible a transition in another state, in which the application can make use of an actuator to reach its goal (switch on the light, play an audio track and so on). To achieve this situation, we need an intermediary between sensor and apps, able to recognize the signal sent by the sensor and create the correct application and actuator to associate. Thus, this is possible thanks to the orchestrator that can associate sensors to application and application to actuators. It can do it with the use of registers that contains this information. In the following interaction diagram, we describe how the interaction between these objects take place: 

![Image description](https://i.ibb.co/mcFSsCB/sequence.png)

Accordingly, the activation of the physical sensors triggers the activation of the software sensor, and we have the same with actuators. Therefore, we choose this approach because it allows the orchestrator to decide which app should be activated based on the inputs received, automatizing the overall process. Another reason is the fact that this approach minimizes the number of sensors used and the number of apps involved for the activation of a sensor.

## 1.2 THE ARCHITECTURE 

A possible identification of the system architecture, also suitable to the IoT, is by the MQTT protocol. It focuses on the principle of publishing messages and subscribing to topics, or "pub/sub". In our case, sensors publish their values that are then received by the applications that made a subscription to that particular sensor. In this case, also, the orchestrator acts as the broker, responsible for distributing messages to recipient clients. But we can, additionally, consider the overall system as an event-driven architecture, in which the principal aim is the production, detection, consumption of, and reaction to events.

![EDA architechture](https://i.ibb.co/gZbKZjQ/EDA-general.jpg)

In our case, the sensors placed in the museum are the event emitter, that have the responsibility to detect, gather, and transfer events. Actuators, instead, are the event consumers, that has the responsibility of applying a reaction as soon as an event manifest. In this image, in particular, we need to clarify components responsibilities:
  
  - Events are generated by the **world**, intended as the museum with visitors that activate sensors.
  - **Context management**, the orchestrator, is responsible to understand from which area comes the notification, what are the visitor 
  preferences or what he might like.
  - **The reasoning component** is still the orchestrator, that has to select the correct application for the notification received.
  - **Behaviour adaptation** is the selected application that based on its current state activates a certain actuator.

This process can also configure as a cycle:

![EDA_proj](https://i.ibb.co/x6hWtz6/Untitled-Diagram.jpg)

We start from the level of devices connection (1), next we sense and collect all this data by sensors (2), and then we communicate them (3).  As soon as the data is collected, we analyze them (4). it is the task of the orchestrator that create knowledge of what is happening in the physical world. This kind of analysis provides to us actionable intelligence (5), and these actions that we get, have a direct impact on the environment, allowing us to interact with it (6). Finally, the software architecture is the following: 

![EDA_proj](https://i.ibb.co/yQ1T40X/UML.jpg)

Where the applications are observers while the orchestrator is a singleton.

## 1.3 SENSORS AND ACTUATORS

Sensors and actuators refer to real sensors and actuators, and for this reason here we provide a description of sensors 
and actuators used:
1. Sensors:
   - **Sensor visitor age**:  we need this sensor to distinguish different ages of visitors, in order to play to them different audio tracks and also to give them different experiences. Therefore, the right solution is the RFID. Indeed, thanks to it, we can transmit information about the age of a visitor. It is possible through a tag attached, for example, on the audio guide provided at the beginning of the visit. 
   ![RFID_reader](https://i.ibb.co/5KQ3MXt/RFID-Illustration.png)
   - **SensorTimer**: The expiration of a simple timer triggers this sensor. We need it to provide further information about a work if the visitor, at the end of the track, wants to know more about that particular work.
  
   - **SensorClock**: We need it to know the time, in order to turn the lights on when it’s dark. Both SensorTimer and SensorClock can be realized using a system call
    
   - **SensorWeather**:A sensor that detects the weather, in this way we can turn the lights on when there are clouds.  It can be a portable cloud sensor. The Portable Cloud Sensor measures the amount of cloud cover by comparing the temperature of the sky to the ambient ground-level temperature. The amount of radiation in the 8 to 14-micron infrared band give us the sky temperature. A large difference indicates clear skies, whereas a small difference means dense, low-level clouds. 
     
     ![cloud_sensor](https://diffractionlimited.com/wp-content/uploads/2016/08/Img_5834.jpg)
     
     Another solution can be using a web service that give continuously the weather. There are several weather APIs, an example can be OpenWeatherMap.
     
   - **SensorPresence**: a simple occupancy sensor (probably a passive infraRed sensor) that detects if there is at least 
     one visitor in the area or none. We need this sensor for the light managing. It is an electronic sensor that 
     measures infrared (IR) light radiating from objects in its field of view.
     
     ![prensence_sensor](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Light_switch_with_passive_infrared_sensor.jpg/150px-Light_switch_with_passive_infrared_sensor.jpg)
   
   - **SensorMobile**: This sensor is triggered at the pushing on a button (placed or in a mobile application or on the audio guide itself), 
     when a visitor need suggestions on works related to the one is currently watching, in this case, a coloured light
     guide him on other works. So even in this case, it is a simple system call 
   
   - **SensorColour and SensorGesture**: These two sensors are related to the pervasive game “chromatize it!” in which a visitor using a device takes a color (in the form of a light source) and uses it to color a wall. So, the sensor color has to detect the color coming out from that light source, and the sensor gesture it’s a motion sensor that detects when a visitor pass the paint on the smart wall. the sensor color can be a SparkFun RGB light sensor - ISL29125. The ISL29125 breakout board makes it very easy to sense and record the light intensity of the general red, green, and blue spectrums of visible light while rejecting IR from light sources.
     
     ![color_sensor](https://cdn.sparkfun.com//assets/parts/9/6/7/7/12829-01.jpg)

2. Actuators:
   
   - **ActuatorAudio**: it is the headphones plugged to the visitor audio-guide, that turn on when a visitor stands in front of an artwork, playing a certain audio track based on the age. The audio-guide has the tag that is detected by the RFID reader. examples can be the following:
     ![audio-guide_RFID](https://sc01.alicdn.com/kf/HTB1ZRmKtyOYBuNjSsD4q6zSkFXaa.jpg)
     
     ![audio-guide_RFID](https://i.ibb.co/N2fVzqK/Schermata-2020-05-18-alle-12-55-08.png)

   - **ActuatorLight**: these are the lights inside the room that turns on or off based on time, weather and presence of a visitor.
   - **ActuatorMobile**: In this case, the actuator can be a mobile or any device to which we can send messages like suggestions on related exhibitions or works, so even the audio-guide itself can be a good actuator.
   - **ActuatorWall**: this is the smart wall that is coloured during the pervasive game ”chromatize it!”
   
     ![smart_wall](https://i.ibb.co/rMCM5kM/Schermata-2020-05-07-alle-10-55-07.png)
    
        so it is a big screen on which the visitor, with the device with the colour, draw something. 
        
   - **ActuatorPainting**: a painting itself can be an actuator, this only in cases of animated works that reproduce what the visitor like most in an exhibition. It can be just a screen that basing on the visitor show different things.
   
   
The code of sensors and actuators is very similar. Indeed, both implements a two-state machine, with the only difference that the sensor has a notify method, that it uses when it is activated. We want to give a generic definition and implementation of sensors and actuators, to have a high degree of independence between them. Indeed, is the orchestrator that makes possible the union of different sensors and actuators. In this way, we have a system in which sensor, actuator, and also applications are not coupled. The code for the 
abstract sensor can be found here: 

https://github.com/huly94/smart_museum_proj/blob/master/smart_proj/Sensors/Sensor.py 

So, every sensor is a state-machine that sends a notification when it is activated. An example of a specific sensor can be the presence sensor. It has two states, empty and not empty, that indicate respectively when there are no visitors in the room and when instead there are. So, the presence of the visitor makes possible the transition from a state to another. Similarly, this is the code for the abstract actuator:

https://github.com/huly94/smart_museum_proj/blob/master/smart_proj/Actuators/Actuator.py

It is simpler because it does not have to notify something. A specific actuator, indeed, is composed by two states: off, when the actuator is inactive, while on when the actuator is active for a state transition triggered by a visitor.
## 1.4 APPLICATIONS

Applications model a certain use case we can have inside the museum. Each scenario, specialized in a particular task, offers particular interactive features, and, mixing all these apps, we have a complete interactive experience. We are going to present them and, then, we will show a table in which we specify the various typologies for each app. Applications are state machines, and the code of the abstract app, that has an update method that is different in every specific application, is the following:

https://github.com/huly94/smart_museum_proj/blob/master/smart_proj/Apps/App.py

### 1.4.1 Audio visitor app
A certain audio track is played based on the visitor age. Different ages have different audio tracks.
 
![avm](https://i.ibb.co/MMynmnm/Schermata-2020-04-23-alle-18-09-39.png)

In this scenario, the visitor that approaches to a work, receive a certain audio basing on his age. This is done
to make more interesting the visit for visitors of all the ages

CODE: https://github.com/huly94/smart_museum_proj/blob/master/smart_proj/Apps/AudioVisitorApp.py 

### 1.4.2 Lights managing app
In this scenario basing on the weather conditions, the time and visitor presence, lights turn on or off. 

![lmm](https://i.ibb.co/VJ2yDfw/Schermata-2020-05-07-alle-12-05-26.png)

This scenario is triggered by the notification of the presence sensor, weather sensor or time sensor, so in the case it's
night or there is a visitor or there are clouds, lights are turned on.

CODE: https://github.com/huly94/smart_museum_proj/blob/master/smart_proj/Apps/LightsManagingApp.py

### 1.4.3 Audio more information app
A visitor receives more information about a work if he spends more time after the end of the track 

![ami](https://i.ibb.co/Jszh24Z/Schermata-2020-05-07-alle-12-08-59.png)

So after the principal track is played, visitors have the opportunity to listen to another track relative to that work,
if they stay contemplating it. So, for example, a visitor that at the end of the track goes to another work, doesn't receive
the additional track, while a visitor that stays for more time receive it.

CODE: https://github.com/huly94/smart_museum_proj/blob/master/smart_proj/Apps/AudioMoreInformationsApp.py

### 1.4.4 Pervasive game "Chromatize It!" 
In an area there are three light sources coloured of different colours, a visitor through a device pick one colour that 
uses to paint a smart wall.

![PG](https://i.ibb.co/b1G0XFT/Schermata-2020-05-07-alle-12-27-18.png)

So in this scenario a visitor using a device (can be still the audio-guide) picks a colour from a light source, then passing
the device on the smart wall, it will be coloured of the selected colour.

CODE: https://github.com/huly94/smart_museum_proj/blob/master/smart_proj/Apps/PervasiveGameChromatizeIt.py

### 1.4.5 Light guide visitor app
A light of a certain color guide a visitor to works he can be interested in.

![lgv](https://i.ibb.co/wLMJ9Ky/Schermata-2020-05-07-alle-12-37-38.png)

In this scenario after that the principal track is played, the user can aks for similar works by pushing a suggestion button
placed on the audio-guide. He will be guided by a coloured light to related works.

CODE: https://github.com/huly94/smart_museum_proj/blob/master/smart_proj/Apps/LightGiudeVisitorApp.py

### 1.4.6 Audio music relax app
During a break a visitor received a relaxing music.

![amr](https://i.ibb.co/qDtWhTL/Schermata-2020-05-07-alle-15-38-06.png)

In this scenario when a visitor is taking a break, so when he is sitting on a bench or he is in a waiting zone, a relaxing music
is played.

CODE: https://github.com/huly94/smart_museum_proj/blob/master/smart_proj/Apps/AudioMusicRelaxApp.py

### 1.4.7 Mobile suggestions app
At the end of the visit, the visitor receives on a device a list of related exhibitions he might like

![msa](https://i.ibb.co/ZWbLNb2/Schermata-2020-05-07-alle-15-52-33.png)

In this scenario a visitor, once that the visit is ended, receive on a device (still the audio-guide) a list of other 
places he might like, basing even on what he liked during the visit.

CODE: https://github.com/huly94/smart_museum_proj/blob/master/smart_proj/Apps/MobileSuggestionsApp.py

### 1.4.8 Interactive work app
This app introduces the possibility for the artists to add interactive works based on visitors emotions or 
preferences

![iwm](https://i.ibb.co/Lr88FkH/Schermata-2020-05-07-alle-17-47-36.png)

This scenario add also interactive works, in the sense that the work is active at the presence of a visitor, displaying 
something like what visitor likes or other properties

CODE: https://github.com/huly94/smart_museum_proj/blob/master/smart_proj/Apps/InteractiveWorkApp.py

Now, we will show the division in typologies of these applications:

![type](https://i.ibb.co/xXZPjd7/Schermata-2020-06-05-alle-10-56-57.png)

## 1.5 THE ORCHESTRATOR

The orchestrator has the task of automating the process of associating sensors with applications, and of applications with actuators. The principal features of the orchestrator are the following: address to the visitor only the applications he needs at that moment and provide a dedicated application for each visitor. The first rise from the fact that the same sensor can have more apps, but we don't need all of them at that moment, so the solution is to divide apps in different areas and then instantiate them basing on in which area the visitor is. An example of a room can be this:

![room_ex](https://i.ibb.co/4s1ZmXp/Schermata-2020-05-07-alle-18-08-18.png)

So, for example, for a visitor in the works area will be created only apps related to the works area. The second feature, instead, works in the following way: at the triggering of the physical sensor we create a software instance of that sensor, relative only to a visitor, and we do the same with the instance of an app, that will be assigned only to that visitor. So, we need to get a reference of the visitor (for example a tag detected by an RFID reader) that we associate to the sensor. In this way, we can have different instances of the same application dedicated to different visitors. Therefore, the final goal of the project is to create a simulation of the reality. it is controlled by the orchestrator according to a specific program, in which sensors and actuator are used to accommodate different applications.

![orch](https://i.ibb.co/94QXf5p/Schermata-2020-05-07-alle-18-06-32.png)