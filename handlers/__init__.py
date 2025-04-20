from .commands import register_commands
from .messages import register_message_handlers
from .callback import register_callback_handlers

def register_handlers(bot):
    register_commands(bot)
    register_message_handlers(bot)
    register_callback_handlers(bot)