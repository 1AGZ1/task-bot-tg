from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

import app.taskManager as tm

async def inline_get_tasks(id, path):
    keyboard = InlineKeyboardBuilder()

    add = 'add' + path

    pathList = await tm.getPathListByPath(id, path)

    if pathList:
        for path_iter in pathList:
            text = await tm.getNameByPath(id, path_iter)

            keyboard.add(InlineKeyboardButton(text=text, callback_data=path_iter))

    keyboard.add(InlineKeyboardButton(text='создать', callback_data=add))

    if path != '/':
        delit = 'del' + path
        keyboard.add(InlineKeyboardButton(text='Удалить', callback_data=delit))

        upper_dir = path[:path.rfind('/', 0, path.rfind('/'))+1]
        keyboard.add(InlineKeyboardButton(text='Назад', callback_data=upper_dir))
    else:
        keyboard.add(InlineKeyboardButton(text='Назад', callback_data='start'))

    return keyboard.adjust(1).as_markup()

async def inline_start():
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text='Задачи', callback_data='task'))
    keyboard.add(InlineKeyboardButton(text='Напоминания', callback_data='reminder'))

    return keyboard.adjust(1).as_markup()

