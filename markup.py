
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton

dnepr_btn = KeyboardButton("Dnipro")
krakow_btn = KeyboardButton("Krakow")
wielichka_btn = KeyboardButton("Wieliczka")

nav_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(dnepr_btn).add(krakow_btn).insert(wielichka_btn)

