class InvalidYearException(Exception):
    def __init__(self, message="L'année est invalide."):
        super().__init__(message)
