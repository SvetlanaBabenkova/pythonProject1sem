class Miles:
    def __init__(self):
        self._state = 'A'
        self._graph = {
            ('A', 'sweep'): ('B', 0),
            ('B', 'sweep'): ('C', 1),
            ('B', 'reset'): ('D', 2),
            ('C', 'punch'): ('D', 3),
            ('C', 'sweep'): ('G', 4),
            ('D', 'sweep'): ('E', 5),
            ('D', 'leer'): ('G', 6),
            ('E', 'sweep'): ('F', 7),
            ('E', 'reset'): ('E', 8),
            ('F', 'reset'): ('G', 9),
            ('F', 'punch'): ('B', 10),
            ('G', 'punch'): ('H', 11),
        }

    def sweep(self):
        self._state, ret_value = self._graph[(self._state, 'sweep')]
        return ret_value

    def punch(self):
        self._state, ret_value = self._graph[(self._state, 'punch')]
        return ret_value

    def reset(self):
        self._state, ret_value = self._graph[(self._state, 'reset')]
        return ret_value

    def leer(self):
        self._state, ret_value = self._graph[(self._state, 'leer')]
        return ret_value


def main():
    return Miles()


o = main()
