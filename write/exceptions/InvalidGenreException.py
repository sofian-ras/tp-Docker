class InvalidGenreException(Exception):
    def __init__(self, message="le genre est invalide."):
        super().__init__(message)
