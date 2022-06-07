class Miles:
    def __init__(self):
        self._state = 'A'
        self._graph = {
            ('A', 'slur'): ('B', 0),
            ('A', 'hop'): ('F', 1),
            ('B', 'hop'): ('C', 2),
            ('B', 'slur'): ('F', 3),
            ('C', 'hop'): ('D', 4),
            ('C', 'slur'): ('G', 5),
            ('D', 'slur'): ('E', 6),
            ('E', 'slur'): ('F', 7),
            ('F', 'slur'): ('G', 8),
            ('G', 'slur'): ('G', 9),
        }
    def slur(self):
        self._state, ret_value = self._graph[(self._state, 'slur')]
        return ret_value
    def hop(self):
        self._state, ret_value = self._graph[(self._state, 'hop')]
        return ret_value
def main():
    return Miles()
o = main()