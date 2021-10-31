"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, num):
        '''two numbers are set, one for init and other for counting'''
        self.start_num = num
        self.counter = num
    def generate(self):
        '''return counter + 1'''
        self.counter += 1
        return self.counter
    def reset(self):
        '''resetting to init val with start_num, and counter set to start_num'''
        self.counter = self.start_num
        return self.start_num
