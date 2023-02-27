"""File contains generic models"""
from pydantic import BaseModel


class Message(BaseModel):
    """Generic message model"""

    msg: str


class GenericSchema:
    """Container class for all generic models"""

    Message: Message = Message
