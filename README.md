# 🕒 Telegram Auto Bio & Name Updater

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Pyrogram](https://img.shields.io/badge/Powered%20by-Pyrogram-green.svg)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

Скрипт обновляет **имя** и **био** вашего Telegram-аккаунта **каждую минуту**:

✅ Время в разных городах (Москва, Токио, Париж)
✅ Курсы криптовалют (BTC, ETH, TON — CoinGecko)
✅ Курсы валют (USD, EUR, CNY — ЦБ РФ)

Основан на **[Pyrogram](https://docs.pyrogram.org/)** и **httpx**.

---

## 📸 Пример

**Имя:**
```
root@Pyrogram:~# 15:42
```

**Bio:**
```
✅Updated every minute┊🇷🇺MSK 15:42┊🇯🇵TYO 21:42┊🇫🇷PAR 14:42┊🟠BTC $67421┊🟣ETH $3280┊🔷TON $5.14┊💵USD 92.31₽┊💶EUR 99.87₽┊💴CNY 12.64₽
```

---

## 🚀 Запуск

```bash
git clone https://github.com/Laur1dor/Telegram-Profile-AutoUpdate.git
cd Telegram-Profile-AutoUpdate
cp .env.example .env      # вписать API_ID и API_HASH
docker compose up -d
```

`API_ID` и `API_HASH` берутся на [my.telegram.org](https://my.telegram.org).

При первом запуске Pyrogram попросит войти в аккаунт — сделайте это
интерактивно, чтобы сохранить сессию:

```bash
docker compose run --rm tgtime python -u main.py
```

Файл сессии останется в `data/` и переиспользуется дальше. Он **приватный**:
кто им владеет, тот владеет аккаунтом. В репозиторий не попадает.

---

## 🌐 Сеть

Telegram-протокол MTProto в ряде сетей режется DPI, поэтому весь трафик —
и MTProto, и запросы к API курсов — идёт через прокси.

| Транспорт | Как включить | Когда |
|---|---|---|
| **Cloudflare WARP** *(по умолчанию)* | ничего не нужно | DPI его не трогает |
| **VLESS** *(опционально)* | `docker compose --profile vless up -d` + `PROXY_URL=socks5://xray:2080` | если у вас есть рабочая нода |

Контейнер `xray` собирает конфиг из подписки или из списка ссылок
(`VLESS_SUBSCRIPTION` / `VLESS_CONFIGS` / `VLESS_CONFIGS_FILE`) и сам обновляет
её по расписанию. Балансировка по задержке, мёртвые ноды выпадают автоматически.

Прямое подключение тоже возможно — оставьте `PROXY_URL` пустым.

---

## ⚙️ Настройки

| Переменная | Назначение |
|---|---|
| `API_ID`, `API_HASH` | ключи приложения с my.telegram.org |
| `PROXY_URL` | SOCKS5-прокси для всего трафика; пусто = напрямую |
| `VLESS_SUBSCRIPTION` | ссылка на подписку для профиля `vless` |
| `VLESS_CONFIGS` | список `vless://` через запятую |
| `VLESS_CONFIGS_FILE` | путь к файлу со ссылками, по одной на строку |
| `VLESS_UPDATE_INTERVAL` | период обновления подписки, секунды (по умолчанию 21600) |

Города, набор валют и формат строки правятся прямо в `main.py` —
функции `get_time`, `fetch_prices`, `fetch_cbr_rates` и `update`.

---

## 🛡 Осторожно

- Telegram ограничивает частоту смены профиля. Скрипт ловит `FloodWait`
  и ждёт столько, сколько попросит сервер.
- Аккаунт используется как обычный пользователь (не бот) — это ваша личная
  сессия. Не публикуйте `data/` и `.env`.

---

## 📄 Лицензия

MIT
