class PlanetFourError(Exception):
    """Base class for exceptions in this module."""
    pass


class NoFilesFoundError(PlanetFourError):

    def __str__(self):
        return "Search or glob for files returned empty."


class NoDataToClusterError(PlanetFourError):

    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        return "No data to scan was found in obj: {}".format(self.obj)


class UnknownMarkingKindError(PlanetFourError):

    def __init__(self, kind):
        self.kind = kind

    def __str__(self):
        return """An unknown marking kind was set: {}. Usually this should be
 one of 'fans' or 'blotches'.""".format(self.kind)
