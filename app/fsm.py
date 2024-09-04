from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

class AddTask(StatesGroup):
    id = State()
    path = State()
    name = State()
    description = State()
