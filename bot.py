import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

categories_to_suppliers = {
    "базар": "Жолдощ базар",
    "алкоголь": "Парадайс",
    "вода": "Шоро",
    "сендвичи": "Венера эже",
    "пепси": "Пепси",
    "пиво": "Тенгри"
}

category_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Отправьте список товаров по категориям, например:\n\n"
        "пиво:\n"
        "mango-1\n"
        "stout-1\n"
        "lager-1"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    try:
        lines = message.split("\n")
        current_category = None

        for line in lines:
            line = line.strip()
            if line.endswith(":"):
                current_category = line[:-1].lower()
                if current_category not in category_data:
                    category_data[current_category] = []
            elif current_category:
                category_data[current_category].append(line)

        await update.message.reply_text("Данные успешно обработаны!")
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")

async def show_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = ""
    for category, items in category_data.items():
        supplier = categories_to_suppliers.get(category, "Неизвестный поставщик")
        response += f"Категория: {category} (Поставщик: {supplier}):\n"
        response += "\n".join(f"- {item}" for item in items) + "\n\n"
    await update.message.reply_text(response if response else "Нет данных.")

async def clear_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    category_data.clear()
    await update.message.reply_text("Все данные очищены!")
app = ApplicationBuilder().token("8016346915:AAHbffp3yGDk_K0ZwjUCTK1VRYRE7o1-UQI").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("show", show_data))
app.add_handler(CommandHandler("clear", clear_data))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен...")
app.run_polling()
