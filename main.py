from asyncio import run
from os import environ
from time import sleep

from aiohttp import ClientSession
from dotenv import load_dotenv

load_dotenv()

tg_token = environ.get("tg_token")
user = environ.get("tg_user")

endway_themes = environ.get("endway_themes").split()
cybhack_themes = environ.get("cybhack_themes").split()
zelenka_themes = environ.get("zelenka_themes").split()

endway_cookie = environ.get("endway_cookie")
endway_token = environ.get("endway_token")

cybhack_token = environ.get("cybhack_token")
cybhack_cookie = environ.get("cybhack_cookie")

zelenka_token = environ.get("zelenka_token")

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"


async def send_message(message: str):
    async with ClientSession() as session:
        data = await session.post(
            url=f"https://api.telegram.org/bot{tg_token}/sendMessage",
            data={
                "chat_id": user,
                "text": message,
                "parse_mode": "HTML"
            }
        )
        json = await data.json()
        print(json)


async def main_loop():
    # endway auto up
    for theme in endway_themes:
        async with ClientSession(headers={
            "Cookie": endway_cookie,
            "User-Agent": user_agent
        }) as session:
            response = await session.post(
                url="https://endway.su/threads/" + theme + "/bump",
                data={
                    "_xfWithData": "1",
                    "_xfToken": endway_token,
                    "_xfResponseType": "json",
                    "_xfRequestUri": "https://endway.su/threads/" + theme
                }
            )
            data = await response.json()
            message = f"""✅ Ап темы https://endway.su/threads/{theme}

⏳ Статус: <b>{data['status']}</b>"""
            if data['status'] == 'error':
                message += f"\n💫 Ошибка: <code>{data['errors'][0]}</code>"
            await send_message(message)
            await session.close()
    # cybhack auto up
    for theme in cybhack_themes:
        async with ClientSession(headers={
            "Cookie": cybhack_cookie,
            "User-Agent": user_agent
        }) as session:
            response = await session.post(
                url="https://cybhack.net/threads/" + theme + "/up",
                data={
                    "_xfWithData": "1",
                    "_xfToken": cybhack_token,
                    "_xfResponseType": "json",
                    "_xfRequestUri": "/threads/" + theme
                }
            )
            data = await response.json()
            message = f"""✅ Ап темы https://cybhack.net/threads/{theme}

⏳ Статус: <b>{data['status']}</b>"""
            if data['status'] == 'error':
                message += f"\n💫 Ошибка: <code>{data['errors'][0]}</code>"
            await send_message(message)
            await session.close()
    # zelenka autobump
    for theme in zelenka_themes:
        async with ClientSession(headers={"Authorization": f"Bearer {zelenka_token}"}) as session:
            response = await session.post(
                url=f"https://api.zelenka.guru/threads/{theme}/bump"
            )
            data = await response.json()
            message = f"""✅ Ап темы https://zelenka.guru/threads/{theme}

⏳ Статус: <b>{"✅ Успешно" if not data.get("errors") else "❌ Ошибка"}</b>"""
            if data.get("errors"):
                error = data['errors'][0].replace("<br>", "\n")
                message += f"\n💫 Ошибка: <code>{error}</code>"
            await send_message(message)
            await session.close()


if __name__ == "__main__":
    while True:
        run(main_loop())
        sleep(86400)
