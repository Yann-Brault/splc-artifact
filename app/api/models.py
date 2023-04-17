from pydantic import BaseModel


class Configuration(BaseModel):
    """
    This class is data model

    Attributes
    ----------
    config : str
        a formatted string that contains the client configuration

    """

    config: str
