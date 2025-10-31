from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup
from aiogram.types import KeyboardButton



def start_kb():
    """кнопка старта"""
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=" Войти в магазин")]],
        resize_keyboard=True
    )