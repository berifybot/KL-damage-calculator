from status import Status

class ElementStats:
    def __init__(self, applied_status: Status):
        self.applied_status = applied_status

    def get_applied_status(self) -> Status:
        return self.applied_status