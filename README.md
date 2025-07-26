# 🕒 Telegram Auto Bio & Name Updater

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)  
![Pyrogram](https://img.shields.io/badge/Powered%20by-Pyrogram-green.svg)  
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

Этот скрипт обновляет **имя** и **био** вашего Telegram-аккаунта **каждую минуту** с актуальной информацией:

✅ Время в разных городах (Москва, Токио, Париж)  
✅ Курсы криптовалют (BTC, ETH, TON)  
✅ Курсы валют (USD, EUR, CNY по данным ЦБ РФ)  

Основан на **[Pyrogram](https://docs.pyrogram.org/)** и **httpx**.

---

## 📸 Пример

**Имя:**  
```
root@pyrogram:~# 15:42
```

**Bio:**  
```
✅Updated every minute┊🇷🇺MSK 15:42┊🇯🇵TYO 21:42┊🇫🇷PAR 14:42┊🟠BTC $64000┊🟣ETH $3200┊🔷TON $6.22┊💵USD 91.32₽┊💶EUR 99.11₽┊💴CNY 12.55₽
```

---

## 🔧 Функционал

✔️ Обновление каждые **60 секунд**  
✔️ Получение данных из:  
- [CoinGecko API](https://www.coingecko.com/en/api) (BTC, ETH, TON)  
- [ЦБ РФ API](https://www.cbr-xml-daily.ru/) (USD, EUR, CNY)  
✔️ Автообновление имени и био через **Telegram API**  
✔️ Обработка ошибок и FloodWait  

---

## 🚀 Установка

### 1. Клонирование репозитория
```bash
git clone https://github.com/Laur1dor/Updated-every-minute-Telegram-Bio-and-Name.git
cd Updated-every-minute-Telegram-Bio-and-Name
```

### 2. Виртуальное окружение и зависимости
```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
pip install -r requirements.txt
```

📄 **requirements.txt**:
```
pyrogram
tgcrypto
httpx
python-dotenv
```

---

## 🔑 Получение API ID и API HASH

1. Перейдите на [my.telegram.org](https://my.telegram.org)  
2. Войдите в аккаунт  
3. Создайте приложение и получите **API ID** и **API HASH**  

---

## ⚙️ Настройка

Создайте файл `.env` в корне проекта:

```
API_ID= 123456
API_HASH= your_api_hash_here
```

> Скрипт автоматически подтянет значения из `.env`.

---

## ▶️ Запуск

```bash
python main.py
```

Скрипт будет работать до ручной остановки.

---

## ❗ Важно

- Telegram может временно ограничить изменения имени/био при слишком частом обновлении. Скрипт учитывает `FloodWait` и ждет нужное время.
- Рекомендуемый интервал: **60 секунд**.

---

## 📜 Лицензия

MIT License

---

## ⭐ Поддержка

Если проект полезен — поставьте ⭐!
