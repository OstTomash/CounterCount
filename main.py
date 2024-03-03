class Counter:
    """A simple class to create Counter.

    This class can be used to count amount of instances, and also can return
    the number of calls method get_count.

    Class attributes:
        - count: an integer representing the amount of instances being created

    Attributes:
        - method_called: an integer representing the amount of calls method get_count

    Methods:
        - __init__: initialize the counter and increase the count by 1,
        and initialized the method_called attribute
        - get_count(): returns the amount of instances being created
        and increments attribute method_called by 1.

    Example usage:
    >>> counter_1 = Counter()
    >>> counter_2 = Counter()
    >>> result_1 = counter_1.get_count()
    >>> result_2 = counter_2.get_count()
    >>> result_3 = counter_2.get_count()
    >>> print(result_1)
    2
    >>> print(result_2)
    2
    >>> print(result_3)
    2
    >>> print(counter_1.method_called)
    1
    >>> print(counter_2.method_called)
    2
    """

    count = 0

    def __init__(self):
        """Initialize the new Counter with attribute method_called and increase the count by 1."""
        Counter.count += 1
        self.method_called = 0

    def get_count(self):
        """Return the amount of instances being created and increase the method_called by 1."""
        self.method_called += 1
        return Counter.count
