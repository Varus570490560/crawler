class TimeOutError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


def throw_time_out_error(arg):
    raise TimeOutError(arg)
