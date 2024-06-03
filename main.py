from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from keyboard import main_menu, filial_buttons, filial_buttons2, filial_buttons3, bosh_ish_orin, bosh_ish_orin2, \
    bosh_ish_orin3, universal_xodim, yunsobod, bahodir, mirzo_ulugbek, yashnobod, yakkasaroy, til

BOT_TOKEN = "6363383894:AAG1hdCI8JkiyCDMmkyesAP2j2YlhS4-NR0"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

evos_photo = "https://tashkent.hh.uz/employer-logo/4136381.jpeg"
evos_photo2 = "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT8USQbUpRk6TFRNgglTH6Y7pnw0pSqHOTgRU5-7EfuOj82HMNI"
evos_photo3 = "https://avatars.mds.yandex.net/get-altay/9793917/2a0000018adb21c26b775cec7aa40f943e6c/L_height"
evos_photo4 = "https://www.afisha.uz/uploads/media/2018/02/0160365.jpeg"
evos_photo5 = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQIS-5Bs2WZay8iidP3mnuZWV4o3Km2NTL6cg2bjWA6O-QOIcbr"
evos_photo6 = "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQR5oWKHaBhXaxilfPywRH99bCNCpRT15VsaGxuS7HHtLX6Z5wM"
evos_photo7 = "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSzSTjC-a6Hg9Z7Xjb6rZSquuSC48RaqrOKInuFshW5Ipklco4W"
evos_photo8 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUS4y1LJ7w92FfZJ_B8qMmwFmlpX0f33vktWgBAVdNNKLs6g_3"
evos_photo9 = "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQMgClrjZaS5WmOAi3GAU1VsM1DQuBL-FfhBNWQ7qvqhb9Cz57w"
evos_photo10 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVFf1zYwlB-le52kuvkPahNdLfn7VxRd98uN6Tb0gAKtf4TRGD"
evos_photo11 = "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQk1vwZlJNBcPDe57i2OKRNeLOX4wE8QHZ6aI1tpc0Kc2Bo2dJy"
evos_photo12 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIH_INk5DO2HUrvloOOsZGMC0vIEVUU_MHlJJsgYv-p4BqSANF"


@dp.message_handler(commands=["start", "help"])
async def start_bot(message: types.Message):
    await message.answer("Botga xush kelibsiz", reply_markup=main_menu())


@dp.message_handler(Text(equals="📍 Fililallar"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo,
                               reply_markup=filial_buttons(),
                               caption="""EVOS - O'zbekistondagi eng yirik fastfud kompaniyasi. Ayni paytda 49 ta chakana savdo shoxobchasi va zamonaviy diversifikatsiyalangan ishlab chiqarish ochiq.

Kompaniya xodimlari birgalikda rivojlanib, kundan -kunga o'sib borayotgan katta oila. EVOS har kuni kengayib bormoqda, bugungi kunda bizda bir yarim mingdan ortiq odam bor. Bizning jamoamizga a'zo bo'ling, EVOS oilasiga xush kelibsiz!""")


@dp.message_handler(Text(equals="🏢 Kompaniya haqida"))
async def star_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo2,
                               reply_markup=main_menu(),
                               caption="""EVOS ® tez xizmat ko'rsatish restoranlari tarmog'i bir joyda turmaydi, siz uchun va siz bilan doimo o'sib boradi va rivojlanadi! Biz geografiyamizni kengaytiramiz va deyarli har oyda yangi filiallarni ochamiz.
Endi bizning tarmog'imizning O'zbekiston bo'ylab 50 dan ortiq filiali mavjud. Biz doimo jamoamizning bir qismi bo'lishni xohlaydigan va EVOS ® da o'z faoliyatini boshlashga tayyor bo'lgan dinamik va faol odamlarni qidiramiz.
EVOS ® –  bu ishonchli brenddir. EVOS ® da ishlash – barqaror daromad va martaba istiqbollari kafolati.
EVOS ® da o'z karyerangizni boshlang!""")


@dp.message_handler(Text(equals="☕️ Yaqin filiallarni ko'rsatish"))
async def stark_bot(message: types.Message):
    await message.answer(text="Энг яқин филиални топиш учун жойлашувингизни юборинг",
                         reply_markup=filial_buttons2())


@dp.message_handler(Text(equals="⬅️ Орқага"))
async def starw_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo4,
                               reply_markup=filial_buttons())


@dp.message_handler(Text(equals="🏢 Bosh ofis"))
async def starw_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo5,
                               caption="""Manzil:  Furqat ko'chasi 175, 1-kirish, 4-qavat.
Mo'ljal: MAKRO THE TOWER

Kontakt: +998712031212""",
                               reply_markup=filial_buttons())
    await message.answer(text="https://maps.google.com/maps?q=41.302196,69.248867&ll=41.302196,69.248867&z=16")


@dp.message_handler(Text(equals="Toshkent sh."))
async def starw_bot(message: types.Message):
    await message.answer(text="Toshkent sh.",
                         reply_markup=filial_buttons3())


@dp.message_handler(Text(equals="📍 Samarqand Darvoza"))
async def starw_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo6,
                               caption="""Filial: "Samarqand Darvoza"

Manzil: Qoratosh, 5A""",
                               reply_markup=filial_buttons3())
    await message.answer(text="https://maps.google.com/maps?q=41.316428,69.230965&ll=41.316428,69.230965&z=16")


@dp.message_handler(Text(equals="📍 Oloy Bozozri"))
async def starw_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo7,
                               caption="""Filial: Oloy bozori

Manzil: Amir Temur prospekti, 42

Kontakt: +998 71 203 12 12""",
                               reply_markup=filial_buttons3())
    await message.answer(text="https://maps.google.com/maps?q=41.320000,69.282572&ll=41.320000,69.282572&z=16")


@dp.message_handler(Text(equals="📍 Malika"))
async def starw_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo8,
                               caption="""Filial: Malika

Manzil: Bog'iravon, 29

Kontakt: +998 71 203 12 12""",
                               reply_markup=filial_buttons3())
    await message.answer(text="https://maps.google.com/maps?q=41.342807,69.264684&ll=41.342807,69.264684&z=16")


@dp.message_handler(Text(equals="📍 Yahyo G'ulomov,94"))
async def starw_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo9,
                               caption="""Filial: Yahyo G'ulomov ko'chasi, 94

Manzil: Yahyo G'ulomov ko'chasi, 94

Kontak: +998 71 203 12 122""",
                               reply_markup=filial_buttons3())
    await message.answer(text="https://maps.google.com/maps?q=41.304758,69.284565&ll=41.304758,69.284565&z=16")


@dp.message_handler(Text(equals="⬅️ Ortga"))
async def stark_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo4,
                               reply_markup=main_menu())


@dp.message_handler(Text(equals="Ortga↩️"))
async def stark_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo4,
                               reply_markup=filial_buttons())


@dp.message_handler(Text(equals="💼 Bo'sh ish o'rinlari"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="EVOS jamoasiga qo'shiling!",
                         reply_markup=bosh_ish_orin())
    await messege.answer(text="📍 Shaharni tanlang.")


@dp.message_handler(Text(equals="Toshkent"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang",
                         reply_markup=bosh_ish_orin2())


@dp.message_handler(Text(equals="Andijon"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang",
                         reply_markup=bosh_ish_orin3())


@dp.message_handler(Text(equals="Qarshi"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang",
                         reply_markup=bosh_ish_orin3())


@dp.message_handler(Text(equals="Qo'qon"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang",
                         reply_markup=bosh_ish_orin3())


@dp.message_handler(Text(equals="Namangan"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang",
                         reply_markup=bosh_ish_orin3())


@dp.message_handler(Text(equals="Toshkent viloyati"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang",
                         reply_markup=bosh_ish_orin3())


@dp.message_handler(Text(equals="Nukus"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang",
                         reply_markup=bosh_ish_orin3())


@dp.message_handler(Text(equals="Samarqand"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang",
                         reply_markup=bosh_ish_orin3())


@dp.message_handler(Text(equals="Farg'ona"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang",
                         reply_markup=bosh_ish_orin3())


@dp.message_handler(Text(equals="Shahrisabz"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang",
                         reply_markup=bosh_ish_orin3())


@dp.message_handler(Text(equals="Xorazm viloyati"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang",
                         reply_markup=bosh_ish_orin3())


@dp.message_handler(Text(equals="Universal xodim"))
async def bosh_bot(messege: types.Message):
    await messege.answer_photo(photo=evos_photo10,
                               caption="""🇷🇺/🇺🇿 Rus va o'zbek tillarni bilish kerak

🕑 Erkin jadval (iloji bo'lsa)

✔️ Yoqimli tashqi ko'rinish

💰 Ish haqi 17228.96 dan (soliqlargacha) bir soatiga""",
                               reply_markup=universal_xodim())
    await messege.answer(text="Hozirda vakansiya ochilgan tumanlardan birini tanlang")


@dp.message_handler(Text(equals="Yunsobod"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="📍 Qaysi filialda ishlashni istaysiz?",
                         reply_markup=yunsobod())


@dp.message_handler(Text(equals="📍 Bahodir"))
async def bosh_bot(messege: types.Message):
    await messege.answer_photo(photo=evos_photo11,
                               caption="Yunusota ko'chasi, 25/24",
                               reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.379405,69.305609&ll=41.379405,69.305609&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="📍 Oloy Bozori"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Toshkent, Amir Temur shoh ko‘chasi, 42-uy",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.320045,69.282388&ll=41.320045,69.282388&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="📍 Yunsobod"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Toshkent, Mayqo‘rg‘on ko‘chasi, 11B",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.360131,69.277341&ll=41.360131,69.277341&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="📍 Universam"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Yunusobod tumani, 4-kvartal, Ahmad Donisha ko‘chasi, 1-uy",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.364632,69.286190&ll=41.364632,69.286190&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="❌ Bekor qilish ❌"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="❌ Bekor qilish ❌",
                         reply_markup=main_menu())


@dp.message_handler(Text(equals="Ortga ↩️"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Ortga ↩️",
                         reply_markup=bosh_ish_orin())


@dp.message_handler(Text(equals="Mirzo Ulug'bek"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="📍 Qaysi filialda ishlashni istaysiz?",
                         reply_markup=mirzo_ulugbek())


@dp.message_handler(Text(equals="📍 Maksim Gorkiy"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="51 Mirzo Ulug'bek shoh ko'chasi, Tashkent, Oʻzbekiston",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.325678,69.324202&ll=41.325678,69.324202&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="📍 Qorasu"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Toshkent, Mirzo-Ulug‘bek tumani, Qorasuv massivi, 3-kvartal, 14B",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.334534,69.370307&ll=41.334534,69.370307&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="📍 Ekobozor savdo markazi"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Toshkent, Timur Malik koʻchasi, 3-uy",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.354120,69.353765&ll=41.354120,69.353765&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="📍 Selxoz"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Toshkent viloyati, Qibray tumani, Salar shaharcha qishlog‘i, Toshkent halqa yo‘li",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.358741,69.339849&ll=41.358741,69.339849&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="📍 TTZ"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Toshkent, Mirzo Ulug‘bek tumani, Beshkapa mahallasi",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.355779,69.376185&ll=41.355779,69.376185&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="Yashnobod"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="📍 Qaysi filialda ishlashni istaysiz?",
                         reply_markup=yashnobod())


@dp.message_handler(Text(equals="📍 Lisunova 2"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Toshkent, Aviasozlar 9/3",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.290595,69.342981&ll=41.290595,69.342981&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="📍 Lisunova"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Aviasozlar 3, 21-bino",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.291741,69.340696&ll=41.291741,69.340696&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="Yakkasaroy"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="📍 Qaysi filialda ishlashni istaysiz?",
                         reply_markup=yakkasaroy())


@dp.message_handler(Text(equals="📍  Shota Rustaveli"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Shota Rustaveli ko'chasi , 36",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.289761,69.257912&ll=41.289761,69.257912&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="📍 Muqimiy"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="O'zbekiston, Toshkent, ko'ch. Muqimiy, 7",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.280094,69.241587&ll=41.280094,69.241587&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals='📍 "Next" Savdo Markazi'))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="O'zbekiston, Toshkent, ko'ch. Muqimiy, 7",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.280094,69.241587&ll=41.280094,69.241587&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="📍  Teatralny"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Yakkasaroy tumani, Bobura ko‘chasi 40A",
                         reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.285577,69.253180&ll=41.285577,69.253180&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="📍  Южный"))
async def bosh_bot(messege: types.Message):
    await messege.answer(
        text="""ТРЦ Vega Centre, ул. Шота Руставели 150 напротив Южного вокзала, 100121, Тоshkent по Zargarlik ko'chasi и Kichik Xalqa Yo'li""",
        reply_markup=bahodir())
    await messege.answer(text="https://maps.google.com/maps?q=41.265794,69.163627&ll=41.265794,69.163627&z=16")
    await messege.answer(text="👤 Ism sharifingizni kiriting?")


@dp.message_handler(Text(equals="Ortga ↩️"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Ortga ↩️",
                         reply_markup=bosh_ish_orin3())


@dp.message_handler(Text(equals="🗣 Yangiliklar"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="""Kompaniya yangiliklari
Aksiya
Yangi filiallar
Yangi tortlar va hk.""",
                         reply_markup=main_menu())


@dp.message_handler(Text(equals="Menyu"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo2,
                               caption="<a href='https://evos.uz/'>Evos saytiga o'tish</a>",
                               parse_mode="HTML")
    await message.answer(
        text="<a href='https://instagram.com/evosuzbekistan/'>Instagram|</a>""<a href='https://t.me/evosdeliverybot/'>Telegram|</a>""<a href='https://facebook.com/evosuzbekistan/'>Facebook</a>",
        parse_mode="HTML")


@dp.message_handler(Text(equals="📞 Kontaktlar/Manzil"))
async def bosh_bot(messege: types.Message):
    await messege.answer_photo(photo=evos_photo12,
                               caption="""Manzil: Furqat ko'chasi 175, kirish 1, 
2-qavat.
Mo'ljal: MAKRO THE TOWER

Kontakt: +998 71 203 12 12""",
                               reply_markup=main_menu())
    await messege.answer(text="https://maps.google.com/maps?q=41.302196,69.248867&ll=41.302196,69.248867&z=16")


@dp.message_handler(Text(equals="🇺🇿/🇷🇺 Til"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="🇺🇿/🇷🇺 Til",
                         reply_markup=til())


@dp.message_handler(Text(equals="🇺🇿 O'zbekcha"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Танланди: 🇺🇿 O'zbekcha",
                         reply_markup=til())


@dp.message_handler(Text(equals="🇷🇺 Русский"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="Выбрано: 🇷🇺 Русский",
                         reply_markup=til())


@dp.message_handler(Text(equals="⬅️ Ortga"))
async def bosh_bot(messege: types.Message):
    await messege.answer(text="⬅️ Ortga",
                         reply_markup=main_menu())


if __name__ == '__main__':
    executor.start_polling(dp)
