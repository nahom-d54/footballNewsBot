from pydantic import BaseModel
from typing import Optional, List

# Define models based on the structure of Telegram's webhook JSON
class User(BaseModel):
    id: int
    first_name: str
    is_bot: bool
    username: Optional[str]

class Chat(BaseModel):
    id: int
    type: str
    username: Optional[str]

class Message(BaseModel):
    message_id: int
    from_user: User
    chat: Chat
    date: int
    text: Optional[str]

class UpdateModel(BaseModel):
    update_id: int
    message: Optional[Message]

# You can add more fields to the model if needed, such as edited_message, inline_query, etc.
