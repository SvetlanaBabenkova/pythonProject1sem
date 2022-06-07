class Miles:
    def __init__(self):
        self._state = 'A'
        self._graph = {
            ('A', 'etch'): ('B', 0),
            ('B', 'merge'): ('C', 1),
            ('B', 'etch'): ('E', 2),
            ('C', 'merge'): ('D', 3),
            ('D', 'align'): ('E', 4),
            ('D', 'etch'): ('G', 5),
            ('E', 'align'): ('F', 6),
            ('F', 'merge'): ('G', 7),
            ('G', 'align'): ('B', 8),
            ('G', 'merge'): ('G', 9),
        }
    def etch(self):
        self._state, ret_value = self._graph[(self._state, 'etch')]
        return ret_value
    def merge(self):
        self._state, ret_value = self._graph[(self._state, 'merge')]
        return ret_value
    def align(self):
        self._state, ret_value = self._graph[(self._state, 'align')]
        return ret_value

def main():
    return Miles()

