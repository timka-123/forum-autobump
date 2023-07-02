# Автоап тем на форумах

## Поддерживаемые форумы

* zelenka.guru
* cybhack.net
* endway.su

## Установка скрипта

```bash
git clone https://github.com/timka-123/forum-autobump
cd forum-autobump
pip install -r requirements.txt
python main.py
```

## Настройка конфига

Создайте файл `.env` и заполните его по образцу с `.env.example`

Разберу по пунктам, что и как заполнять:

* `tg_token` - токен тг бота, куда будут идти уведомления
* `tg_user` - ID пользователя, кому будут приходить уведомления о циклах апа
* `zelenka_token` - ваш OAuth токен Zelenka.guru. Вы можете получить его [здесь](https://zelenka.guru/account/authorize?client_id=1rrspe9aiw&response_type=token&scope=basic+read+post) (потребуется скопировать токен из строки браузера)
* `endway_cookie` - ваши Cookie файлы Endway
* `endway_token` - ваш токен EndWay, посмотрите в любом POST запросе под ключом `_xfToken`
* `cybhack_token` - ваш токен Cybhack, посмотрите в любом POST запросе под ключом `_xfToken`
* `cybhack_cookie` - ваши Cookie файлы Cybhack
* `endway_themes` - список ID тем, которые нужно апать через пробел. (https://endway.su/threads/id/)
* `cybhack_themes` - список ID тем, которые нужно апать через пробел. (https://cybhack.su/threads/id/)
* `zelenka_themes` - список ID тем, которые нужно апать через пробел. (https://zelenka.guru/threads/id/)


###### Сделано [timka123](https://t.me/t1wk4), 2023 год
