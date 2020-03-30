
import smart_proj.Sensors.SensorVisitorAge
import smart_proj.Sensors.SensorVisitor
import smart_proj.Sensors.SensorTimer
import smart_proj.Sensors.SensorWeather
import smart_proj.Sensors.SensorColors
import smart_proj.Sensors.SensorGesture
import smart_proj.Sensors.SensorClock
import smart_proj.Sensors.SensorMobile
import smart_proj.State_machines.AudioVisitorApp
import smart_proj.Orchestrator.Orchestrator

if __name__ == '__main__':
    sv1 = smart_proj.Sensors.SensorVisitor.SensorVisitor()
    sva1 = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()
    st1 = smart_proj.Sensors.SensorTimer.SensorTimer()
    sm1 = smart_proj.Sensors.SensorMobile.SensorMobile()
    sw = smart_proj.Sensors.SensorWeather.SensorWeather()


    sm1.set_user("1")
    sm1.setArea("Works area")

    sv1.set_user("1")
    sv1.setArea("Works area")
    st1.set_user("1")

    sva1.set_user("1")
    sva1.setArea("Works area")

    sv1.run("visitor_arrived")
    sva1.run("visitor_u18_arrived")
    st1.run("end_timer")

    sv1.run("visitor_left")
    sva1.run("visitor_u18_left")


    #print(smart_proj.Orchestrator.Orchestrator.Orchestrator.get_observers(smart_proj.Orchestrator.Orchestrator.Orchestrator.getInstance()))

    sv1.setArea("Interactive work area")
    sv1.run("visitor_arrived")
    sv1.run("visitor_left")

    sv1.setArea("Relax area")
    sv1.run("visitor_arrived")
    sv1.run("visitor_left")

    sv1.setArea("Works area")
    sv1.run("visitor_arrived")
    sva1.run("visitor_u18_arrived")

    sv1.run("visitor_left")
    sva1.run("visitor_u18_left")

    sm1.run("signal_sent")
    sm1.run("reset")

    sv1.setArea("Exit area")
    sv1.run("visitor_arrived")








