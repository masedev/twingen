from flask import Flask


class Driver:

    def __init__(self):
        self.app = Flask()


    def inizialize(self):
        @self.app.route('/outbound/getData/<int:period>')
        def getDataPeriod(period: int):
            # period is a string of the datetime in the past from the difference between two datetime
            return 200 # TODO return the JSON format of the data between the period specified in the url
        
        @self.app.route('/inbound/hibernate/<int:period>')
        def hibernate(period: int ):
            # this API provides a stop method to hibernate the fingers status and stop the continous movement for a specific time period
            return 0
    
        @self.app.route('/inbound/reset')
        def reset():
            # this API resets fingers values that return gradually to the starting position (default values)
            return 0
        
        @self.app.route('/inbound/press/<int:pressure_level>')
        def press(pressure_level: int ):
            # this API provides a pressure improvememnt or decrement for the finger pressure according to the twin status
            return 
        
        @self.app.route('/inbound/check_healthy')
        def check_external_healthy():
            # healthy check status for the fingers driver
            return 0
        
        
    
        def check_internal_healthy(self):
            # method to check the healthy of the driver in case of rollback from the outbound communication
            # TODO: try a reconnection mechanism for the e2e communication
            return 0


