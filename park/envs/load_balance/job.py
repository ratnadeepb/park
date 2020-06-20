
class Job(object):
    def __init__(self, size, arrival_time):
        self.size = size
        self.arrival_time = arrival_time
        self.server = None
        self.start_time = None
        self.finish_time = None
        # Deep added
        # later we will get queue length of the server
        # when the job was scheduled on it
        # and the time it took to complete the job
        self.q_length = 0
