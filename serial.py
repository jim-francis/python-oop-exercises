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
    def __init__(self, start=0):
        """
        Use generate to increment a number beginning at start
        """
        self.start = self.next = start

    def __repr__(self):
        return f"SerialGenerator start={self.start}"

    def generate(self):
        """
        Return next sequential number
        """
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """
        Return to original starting number
        """
        self.next = self.start
