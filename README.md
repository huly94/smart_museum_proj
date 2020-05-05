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
transition in another state in which the application can make use of an actuator to reach its goal (switch on the light, play an audio track and so on). To achieve this situation we need intermediary between sensor and apps, able to recognize the signal sent by the sensor and create the correct application and actuator to associate. this is possible thanks to a register, that the orchestrator has, that is composed by two maps: one has a sensor as key and as value the list of app associated, the other one has an application as key and as value the list of actuators related. In the following interaction diagram we describe how the interaction between objects take place:
![Image description](https://i.ibb.co/mcFSsCB/sequence.png)