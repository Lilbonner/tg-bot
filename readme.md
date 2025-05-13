# Telegram Bot for Managing Categories and Suppliers

This Telegram bot helps manage categorized lists of items and associates them with specific suppliers. Users can input item lists by category, view the data, and clear it when needed.

## Features
- **Add Items by Category**: Input items under specific categories.
- **View Data**: Display all stored categories, items, and their associated suppliers.
- **Clear Data**: Reset all stored data.

## Categories and Suppliers
The bot supports the following categories and their corresponding suppliers:

| Category   | Supplier          |
|------------|-------------------|
| базар      | Жолдощ базар      |
| алкоголь   | Парадайс          |
| вода       | Шоро              |
| сендвичи   | Венера эже        |
| пепси      | Пепси             |
| пиво       | Тенгри            |

## Installation
1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install dependencies**:
   ```bash
   pip install python-telegram-bot
   ```

3. **Set up the bot token**:
   Replace the placeholder token in `bot.py` with your Telegram bot token:
   ```python
   app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
   ```

## Usage
1. **Start the bot**:
   ```bash
   python bot.py
   ```

2. **Interact with the bot**:
   - Send `/start` to see the welcome message and usage instructions.
   - Send item lists in the following format:
     ```
     пиво:
     mango-1
     stout-1
     lager-1
     ```
   - Use `/show` to display all stored data.
   - Use `/clear` to remove all stored data.

## Example Workflow
1. Send the following message to the bot:
   ```
   пиво:
   lager-1
   stout-2
   ```
2. Use `/show` to display the data:
   ```
   Категория: пиво (Поставщик: Тенгри):
   - lager-1
   - stout-2
   ```
3. Use `/clear` to reset the data.

## Error Handling
- The bot provides user-friendly error messages if the input format is incorrect.

## License
This project is licensed under the MIT License.

## Acknowledgments
This bot uses the ` python-telegram-bot ` library for Telegram API integration.

---
For any issues or feature requests, feel free to open an issue on the repository or contact the developer.

