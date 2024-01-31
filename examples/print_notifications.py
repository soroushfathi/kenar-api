import os

from gunicorn.app.base import Application

from kenar.bot import Bot
from kenar.botmessage import BotMessage
from kenar.handler import ChatNotificationHandler, ChatMessagePayload
from kenar.markup import Markup

api_key = os.environ.get("KENAR_API_KEY")
identification_key = os.environ.get("KENAR_IDENT_KEY")

bot = Bot(api_key, identification_key)


class PrintChatNotificationHandler(ChatNotificationHandler):
    def handle_chat_message(self, timestamp: int, payload: ChatMessagePayload):
        print(payload)
        self.bot.send_bot_message(payload.sender.id, BotMessage(payload.data.text, markups=[Markup("salam", {})]))


bot.add_handler(PrintChatNotificationHandler())


def main():
    class WSGIServer(Application):
        def init(self, parser, opts, args):
            pass

        def load(self):
            return bot

    WSGIServer().run()


if __name__ == '__main__':
    main()
