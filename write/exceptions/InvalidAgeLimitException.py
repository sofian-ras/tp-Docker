class InvalidAgeLimitException(Exception):
    def __init__(self, message="l'age limite est invalide."):
        super().__init__(message)
