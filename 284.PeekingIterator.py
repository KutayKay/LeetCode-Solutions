class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.i = iterator
        self.buf = [self.i.next()] if self.i.hasNext() else []

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.buf[0]

    def next(self):
        """
        :rtype: int
        """
        v = self.buf.pop(0)
        if self.i.hasNext():
            self.buf.append(self.i.next())
        return v

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.buf) > 0

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].