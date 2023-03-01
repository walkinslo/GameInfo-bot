class NoGameOrInvalidInput(Exception):
    """Exception raised when there is no game.
    
    Attributes:
        status - request status code.
        message - explanation.
    """

    def __init__(self, status, message="There's no such game."):
        self.status = status
        self.message = message
        super().__init__(self.message)

        