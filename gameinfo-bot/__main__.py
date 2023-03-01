import logging

from telegram.ext import (
	ApplicationBuilder,
	CommandHandler,
	MessageHandler,
	filters
)

import handlers, config


COMMAND_HANDLERS = {
	"start": handlers.start,
	"status": handlers.status
}


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


if not config.TELEGRAM_BOT_API:
	raise ValueError(
		"TELEGRAM_BOT_API is not set in env. Please set it and try again."
		)


def main():
	app = ApplicationBuilder().token(config.TELEGRAM_BOT_API).build()

	for command_name, command_handler in COMMAND_HANDLERS.items():
		app.add_handler(CommandHandler(command_name, command_handler))

	app.run_polling()


if __name__ == "__main__":
	try: 
		main()
	except Exception:
		import traceback 
		logger.warning(traceback.format_exc())