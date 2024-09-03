from aiogram import F, Router

from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb
import app.taskManager as tm

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

class AddTask(StatesGroup):
    id = State()
    path = State()
    name = State()
    description = State()


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет!!",
        reply_markup = await kb.inline_start()
    )

@router.message(F.data == 'start')
async def callback_start(message: Message):
    await message.answer(
        "Привет!!",
        reply_markup = await kb.inline_start()
    )

# =======================================================

@router.callback_query(F.data.startswith('add'))
async def task_add_first(callback: CallbackQuery, state: FSMContext):
    id = callback.message.from_user.id

    print(callback.data)
    path = callback.data[3:]

    await state.update_data(id=id)
    await state.update_data(path=path)

    await state.set_state(AddTask.name)
    await callback.message.edit_text('Введите название задания:')

@router.message(AddTask.name)
async def task_add_second(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(AddTask.description)
    await message.answer('Введите его описание')

@router.message(AddTask.description)
async def task_add_third(message: Message, state: FSMContext):
    await state.update_data(description=message.text)

    data = await state.get_data()

    print(data)

    new_path = data['path']+data['name']+'/'

    obj = {
        'name': data['name'],
        'description': data['description']
    }

    await tm.addObjByPath(data['id'], obj, new_path)

    await message.answer(
        "Привет!!",
        reply_markup = await kb.inline_get_tasks(
            data['id'],
            data['path']
        )
    )



@router.callback_query(F.data.startswith('del'))
async def task_del(callback: CallbackQuery):
    id = callback.message.from_user.id
    path = callback.data[3:]

    await tm.delObjByPath(id, path)

    new_path = path[:path.rfind('/', 0, path.rfind('/'))+1]

    if new_path != '/':
        await callback.message.edit_text(
            f'''
                Задача: {await tm.getNameByPath(id, new_path)}
                Описание: {await tm.getDescriptionByPath(id, new_path)}
            ''',
            reply_markup = await kb.inline_get_tasks(
                id,
                new_path
            )
        )
    else:
        await callback.message.edit_text(
            'Ваши задачи:',
            reply_markup = await kb.inline_get_tasks(
                callback.message.from_user.id,
                path
            )
        )

@router.callback_query(F.data.startswith('/'))
async def task_get(callback: CallbackQuery):
    id = callback.message.from_user.id
    path = callback.data

    await callback.message.edit_text(
        f'''
            Задача: {await tm.getNameByPath(id, path)}
            Описание: {await tm.getDescriptionByPath(id, path)}
        ''',
        reply_markup = await kb.inline_get_tasks(
            id,
            path
        )
    )

@router.callback_query(F.data == 'task')
async def task_start(callback: CallbackQuery):
    id = callback.message.from_user.id
    path = '/'

    await callback.message.edit_text(
        'Ваши задачи:',
        reply_markup = await kb.inline_get_tasks(
            callback.message.from_user.id,
            path
        )
    )

# ===============================================================
