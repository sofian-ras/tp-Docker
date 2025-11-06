class InvalidTitleException(Exception):
    def __init__(self, message="Le titre est invalide."):
        super().__init__(message)
