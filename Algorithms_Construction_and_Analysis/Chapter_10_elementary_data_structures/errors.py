class StackOverflowError(Exception):

    def __init__(self, msg='Stack is overflowed!', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class StackUnderflowError(Exception):

    def __init__(self, msg='Stack is underflowed!', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class EmptyQueueError(Exception):

    def __init__(self, msg='Queue is empty!', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class QueueOverflowedError(Exception):

    def __init__(self, msg='Queue if overflowed!', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
