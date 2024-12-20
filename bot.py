from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

purchase_orders = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот для обработки закупок. Отправьте мне список товаров.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    try:
        orders = message.split("\n")
        for order in orders:
            parts = order.split(" - ")
            if len(parts) == 3:
                item, quantity, supplier = parts[0], parts[1], parts[2]
                if supplier not in purchase_orders:
                    purchase_orders[supplier] = []
                purchase_orders[supplier].append({"item": item, "quantity": quantity})
        await update.message.reply_text("Закупка успешно обработана!")
        print(purchase_orders)
    except Exception as e:
        await update.message.reply_text(f"Ошибка обработки: {e}")

async def show_orders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = ""
    for supplier, orders in purchase_orders.items():
        response += f"Поставщик {supplier}:\n"
        for order in orders:
            response += f"- {order['item']} ({order['quantity']})\n"
    await update.message.reply_text(response if response else "Нет данных.")

app = ApplicationBuilder().token("8016346915:AAHbffp3yGDk_K0ZwjUCTK1VRYRE7o1-UQI").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("show", show_orders))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен...")
app.run_polling()
