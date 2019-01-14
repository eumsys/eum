import threading

class RecurringTimer(threading._Timer):
    """ Own implementation of timer to make it recurring
 
    Timer (based on threading._Timer)
    that invokes a method at a certain interval of seconds
 
    """
     
    def __init__ (self, *args, **kwargs):
        threading._Timer.__init__ (self, *args, **kwargs) 
        self.setDaemon (True)
        self._running = 0
        self._destroy = 0
        self.start()
        
	def __del__(self):
		self.destroy_timer()
		
    def run (self):
        while True:
            self.finished.wait (self.interval)
            if self._destroy:
                return;
            if self._running:
                #self.function (*self.args, **self.kwargs)
                self.function (*self.args)
 
    def start_timer (self):
        self._running = 1
 
    def stop_timer (self):
        self._running = 0
 
    def is_running (self):
        return self._running
 
    def destroy_timer (self):
        self._destroy = 1;
