from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🏢 Kompaniya haqida"), KeyboardButton(text="📍 Fililallar"))
    rkm.row(KeyboardButton(text="💼 Bo'sh ish o'rinlari"))
    rkm.row(KeyboardButton(text="Menyu"), KeyboardButton(text="🗣 Yangiliklar"))
    rkm.row(KeyboardButton(text="📞 Kontaktlar/Manzil"), KeyboardButton(text="🇺🇿/🇷🇺 Til"))
    return rkm


def filial_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="☕️ Yaqin filiallarni ko'rsatish"))
    rkm.row(KeyboardButton(text="🏢 Bosh ofis"), KeyboardButton(text="Toshkent sh."))
    rkm.row(KeyboardButton(text="⬅️ Ortga"), )
    return rkm


def filial_buttons2():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Geolokatsiyani yuboring", request_location=True))
    rkm.row(KeyboardButton(text="⬅️ Орқага"))
    return rkm


def filial_buttons3():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Samarqand Darvoza"), KeyboardButton(text="📍 Oloy Bozozri"))
    rkm.row(KeyboardButton(text="📍 Malika"), KeyboardButton("📍 Yahyo G'ulomov,94"))
    rkm.row(KeyboardButton(text="Ortga↩️"))
    return rkm


def bosh_ish_orin():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Toshkent"), KeyboardButton(text="Andijon"))
    rkm.row(KeyboardButton(text="Qarshi"), KeyboardButton(text="Qo'qon"))
    rkm.row(KeyboardButton(text="Namangan"), KeyboardButton(text="Toshkent viloyati"))
    rkm.row(KeyboardButton(text="Nukus"), KeyboardButton(text="Samarqand"))
    rkm.row(KeyboardButton(text="Farg'ona"), KeyboardButton(text="Shahrisabz"))
    rkm.row(KeyboardButton(text="Xorazm viloyati"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="⬅️ Ortga"))
    return rkm


def bosh_ish_orin2():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Universal xodim"), KeyboardButton(text="Call-markaz operatori"))
    rkm.row(KeyboardButton(text="Kuryer"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️"))
    return rkm


def bosh_ish_orin3():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Universal xodim"), KeyboardButton(text="Kuryer"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️"))
    return rkm


def universal_xodim():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Yunsobod"), KeyboardButton(text="Mirzo Ulug'bek"))
    rkm.row(KeyboardButton(text="Yashnobod"), KeyboardButton(text="Yakkasaroy"))
    rkm.row(KeyboardButton(text="Uchtepa"), KeyboardButton(text="Sergeli"))
    rkm.row(KeyboardButton(text="Chilonzor"), KeyboardButton(text="Mirobod"))
    rkm.row(KeyboardButton(text="Yashnobod"), KeyboardButton(text="Yakkasaroy"))
    rkm.row(KeyboardButton(text="Bektemir"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️"))
    return rkm


def yunsobod():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Bahodir"), KeyboardButton(text="📍 Oloy Bozori"),
            KeyboardButton(text="📍 Yunsobod"))
    rkm.row(KeyboardButton(text="📍 Universam"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️"))
    return rkm


def mirzo_ulugbek():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Parkent"), KeyboardButton(text="📍 Maksim Gorkiy"),
            KeyboardButton(text="📍 Qorasu"))
    rkm.row(KeyboardButton(text="📍 Ekobozor savdo markazi"), KeyboardButton(text="📍 Selxoz"),
            KeyboardButton(text="📍 TTZ"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️"))
    return rkm


def yashnobod():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Lisunova 2"), KeyboardButton(text="📍 Lisuniva"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️"))
    return rkm


def yakkasaroy():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍  Shota Rustaveli"), KeyboardButton(text="📍 Muqimiy"),
            KeyboardButton(text='📍 "Next" Savdo Markazi'))
    rkm.row(KeyboardButton(text="📍  Teatralny"), KeyboardButton(text="📍 Южный"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️"))
    return rkm


def til():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🇺🇿 O'zbekcha"), KeyboardButton(text="🇷🇺 Русский"))
    rkm.row(KeyboardButton(text="⬅️ Ortga"))
    return rkm


def bahodir():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️"))
    return rkm
