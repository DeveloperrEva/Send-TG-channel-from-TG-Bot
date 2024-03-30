from aiogram.dispatcher.filters.state import State, StatesGroup

class channel(StatesGroup):
    send = State()
    
class add(StatesGroup):
    chan = State()