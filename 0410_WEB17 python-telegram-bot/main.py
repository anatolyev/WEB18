# 4. Импортируем необходимые классы.
import logging
from telegram.ext import Application, MessageHandler, filters

# 4. BOT_TOKEN,                # 11. API_KEY
from config import BOT_TOKEN, API_KEY

# 6. Добавим необходимый объект из модуля telegram.ext
from telegram.ext import CommandHandler

# 7. нужно импортировать его из модуля telegram:
from telegram import ReplyKeyboardMarkup

# 9. Создание сценариев диалогов
from telegram.ext import ConversationHandler

# 11. Поскольку наш телеграм бот работает в асинхронном режиме,
# то применять стандартную библиотеку requests для обращения к сторонним
# api неправильно. Будем применять асинхронную библиотеку aiohttp,
import aiohttp

# 4. Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# 4. Определяем функцию-обработчик сообщений.
# У неё два параметра, updater, принявший сообщение и контекст - дополнительная информация о сообщении.
async def echo(update, context):

    # 11. Добавим клавиатуру и в echo
    markup = await keyboard1()

    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    await update.message.reply_text(update.message.text, reply_markup=markup)

    print(update.message.text)
    print(update.message.from_user)
    print(update.message.sender_chat)

# 7. Напишем функцию клавиатуры:
async def keyboard1():
    """ Создает клавиатуру 1"""

    # 7.
    reply_keyboard = [['/address', '/phone'],
                      ['/site', '/work_time'],
                      # 8.
                      ['/set 5', '/set 10', '/set 60', '/unset'],
                      # 9.
                      ['/survey', '/stop'],
                      ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    return markup


# 6. Их сигнатура и поведение аналогичны обработчикам текстовых сообщений.
async def start(update, context):
    """Отправляет сообщение когда получена команда /start"""
    # 7. Включаем клавиатуру при старте
    markup = await keyboard1()
    # 6.
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я эхо-бот." 
        rf"Напишите мне что-нибудь, и я пришлю это назад!",
        # 7.
        reply_markup=markup
    )


# 6. Напишем соответствующие функции.
async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")

# 7. Напишем соответствующие функции.
async def help(update, context):
    await update.message.reply_text(
        "Я бот справочник.")

# 7. Напишем соответствующие функции.
async def address(update, context):
    await update.message.reply_text(
        "Адрес: г. Москва, ул. Льва Толстого, 16")

# 7. Напишем соответствующие функции.
async def phone(update, context):
    await update.message.reply_text("Телефон: +7(495)776-3030")

# 7. Напишем соответствующие функции.
async def site(update, context):
    await update.message.reply_text(
        "Сайт: http://www.yandex.ru/company")

# 7. Напишем соответствующие функции.
async def work_time(update, context):
    await update.message.reply_text(
        "Время работы: круглосуточно.")




# 8.
async def task(context):
    """Выводит сообщение"""
    job = context.job
    await context.bot.send_message(context.job.chat_id, text=f'КУКУ! {int(job.data)}cек. прошли!')


# 8. Можно взять заготовку со страницы:  https://docs.python-telegram-bot.org/en/stable/examples.timerbot.html
# Обычный обработчик, как и те, которыми мы пользовались раньше.
async def set_timer(update, context):
    """Добавляем задачу в очередь"""
    chat_id = update.effective_message.chat_id
    try:
        # args[0] should contain the time for the timer in seconds
        due = float(context.args[0])
        if due < 0:
            await update.effective_message.reply_text(f"Простите, но мы не можем вернуться в прошлое на {int(due)}сек.!")
            return

        job_removed = remove_job_if_exists(str(chat_id), context)
        context.job_queue.run_once(task, due, chat_id=chat_id, name=str(chat_id), data=due)

        text = f"Таймер на {int(due)}с. установлен!"

        if job_removed:
            text += f" Предыдущий таймер был удален."
        await update.effective_message.reply_text(text)

    except (IndexError, ValueError):
        await update.effective_message.reply_text("Используй: /set <секунд>")

# 8.
async def unset(update, context):
    """Удаляет задачу, если пользователь передумал"""
    # job = context.job
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = f'Таймер отменен!' if job_removed else 'У вас нет активных таймеров'
    await update.message.reply_text(text)

# 8.
def remove_job_if_exists(name, context):
    """Удаляем задачу по имени.
    Возвращаем True если задача была успешно удалена."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


# 9.
async def survey(update, context):
    print("survey запущен")
    await update.message.reply_text(
        "Привет. Пройдите небольшой опрос, пожалуйста!\n"
        "Вы можете прервать опрос, послав команду /stop.\n"
        "В каком городе вы живёте?")

    # Число-ключ в словаре states —
    # втором параметре ConversationHandler'а.
    return 1
    # Оно указывает, что дальше на сообщения от этого пользователя
    # должен отвечать обработчик states[1].
    # До этого момента обработчиков текстовых сообщений
    # для этого пользователя не существовало,
    # поэтому текстовые сообщения игнорировались.

# 9.
async def first_response(update, context):
    # Это ответ на первый вопрос.
    # Мы можем использовать его во втором вопросе.
    # locality = update.message.text - исправляем на словарь!
    # 10. Сохраняем ответ в словаре.
    context.user_data['locality'] = update.message.text
    await update.message.reply_text(
        f"Какая погода в городе {context.user_data['locality']}?")  # Исправляем на словарь
    # Следующее текстовое сообщение будет обработано
    # обработчиком states[2]
    return 2

# 9.
async def second_response(update, context):
    # Ответ на второй вопрос.
    # Мы можем его сохранить в базе данных или переслать куда-либо.
    weather = update.message.text
    logger.info(weather)
    # 9.
    # await update.message.reply_text(f"Привет городу {context.user_data['locality']}!")

    # 11. Добавляем одноразовую клавиатуру:
    reply_keyboard = [['да', 'нет']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_html("Хотите увидеть свой город на карте?",
                                    reply_markup=markup)
    # 10. Очищаем словарь
    # context.user_data.clear()  # очищаем словарь с пользовательскими данными
    # 11.
    # Теперь не очищаем словарь в этом месте, т.к. нам нужно
    # взять эти данные для этого пользователя в функции geocoder
    return 3
    # Все обработчики из states и fallbacks становятся неактивными.

# 9.
async def stop(update, context):
    await update.message.reply_text("Опрос остановлен!")
    return ConversationHandler.END


# 11.
def get_ll_spn(toponym):
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и Широта :
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    # Собираем координаты в параметр ll
    ll = ",".join([toponym_longitude, toponym_lattitude])

    # Рамка вокруг объекта:
    envelope = toponym["boundedBy"]["Envelope"]

    # левая, нижняя, правая и верхняя границы из координат углов:
    l, b = envelope["lowerCorner"].split(" ")
    r, t = envelope["upperCorner"].split(" ")

    # Вычисляем полуразмеры по вертикали и горизонтали
    dx = abs(float(l) - float(r)) / 2.0
    dy = abs(float(t) - float(b)) / 2.0

    # Собираем размеры в параметр span
    span = f"{dx},{dy}"

    return ll, span

# 11.
async def geocoder(update, context):
    print("Геокодер запущен!")

    if update.message.text == "да":
        geocoder_uri = "http://geocode-maps.yandex.ru/1.x/"
        response = await get_response(geocoder_uri, params={
            "apikey": API_KEY,
            "format": "json",
            "geocode": context.user_data['locality']
        })
        print(response)
        if response["response"]["GeoObjectCollection"]["featureMember"]:
            toponym = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            ll, spn = get_ll_spn(toponym)
            # Можно воспользоваться готовой функцией,
            # которую предлагалось сделать на уроках, посвящённых HTTP-геокодеру.

            static_api_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&spn={spn}&l=map"
            await context.bot.send_photo(
                update.message.chat_id,  # Идентификатор чата. Куда посылать картинку.
                # Ссылка на static API, по сути, ссылка на картинку.
                # Телеграму можно передать прямо её, не скачивая предварительно карту.
                static_api_request,
                caption="Вот Ваш город!"
            )
        else:
            # Посылаем ответ, что ничего не найдено или ошибка
            await update.message.reply_text("Ничего не нашли или произошла ошибка.")

    # 11. Возвращем клавиатуру
    markup = await keyboard1()
    await update.message.reply_text("Продлжаем разговор...", reply_markup=markup)

    return ConversationHandler.END  # Константа, означающая конец диалога.

# 11.
async def get_response(url, params):
    logger.info(f"getting {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json()


# 4.
def main():
    # 4. Создаём объект Application.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    application = Application.builder().token(BOT_TOKEN).build()

    # 6. Зарегистрируем их в приложении перед
    # регистрацией обработчика текстовых сообщений.
    # Первым параметром конструктора CommandHandler я
    # вляется название команды.
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # 7.
    application.add_handler(CommandHandler("address", address))
    application.add_handler(CommandHandler("phone", phone))
    application.add_handler(CommandHandler("site", site))
    application.add_handler(CommandHandler("work_time", work_time))
    application.add_handler(CommandHandler("help", help))

    # 8.
    application.add_handler(CommandHandler("set", set_timer,
                                           has_args=True))
    application.add_handler(CommandHandler("unset", unset))

    # 11.
    application.add_handler(CommandHandler("geocoder", geocoder))

    # 9.
    # application.add_handler(CommandHandler("stop", stop)) - это делать нельзя т.к. это точка прерывания диаалога
    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('survey', survey)],

        # Состояние внутри диалога.
        # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.

        states={
            # 9. Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_response)],
            # 9. Функция читает ответ на второй вопрос и задает третий про карту.
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, second_response)],
            # 11. Функция читает ответ третий вопрос и завершает диалог.
            3: [MessageHandler(filters.TEXT & ~filters.COMMAND, geocoder)],
        },
        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
    application.add_handler(conv_handler)

    # 4. Создаём обработчик сообщений типа filters.TEXT
    # из описанной выше асинхронной функции echo()
    # После регистрации обработчика в приложении
    # эта асинхронная функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    # 4. text_handler = MessageHandler(filters.TEXT, echo)

    # 6. Также откорректируем строку, запишем ее так:
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)

    # 4. Регистрируем обработчик в приложении.
    application.add_handler(text_handler)

    # 4. Запускаем приложение.
    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()

