class TimeOutError(RuntimeError):
    def __init__(self):
        pass


def throw_time_out_error():
    raise TimeOutError()
