class ElementStats:
    def __init__(self, applied_status: str):
        self.applied_status = applied_status

    def get_applied_status(self) -> str:
        return self.applied_status