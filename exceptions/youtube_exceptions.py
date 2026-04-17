class YouTubeException(Exception):
    pass


class InvalidURLException(YouTubeException):
    pass


class DownloadException(YouTubeException):
    pass


