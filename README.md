
# 🚀 Маркетплейс Pingera: Шаблоны проверок и Статус Страниц

Этот репозиторий содержит **идеи и готовые шаблоны** для создания проверок и Статус Страниц на платформе [**Pingera**](https://pingera.ru).

> 💡 **Поделитесь своими идеями!** Отправьте **Pull Request** с вашими шаблонами проверок.

---

## 📚 Каталог проверок

### 🔄 [Многошаговые проверки (Multistep)](./multistep/)
Сложные сценарии тестирования API и бизнес-процессов с использованием Playwright.

**[📖 Посмотреть все многошаговые проверки →](./multistep/README.md)**

**Возможности:**
- ✅ Последовательные HTTP-запросы
- ✅ Тестирование API endpoints
- ✅ Проверка CRUD операций
- ✅ Аутентификация через секреты

### 🎭 [Синтетические проверки (Synthetic)](./synthetic/)
Тестирование пользовательских сценариев и веб-интерфейсов в браузере.

**[📖 Посмотреть все синтетические проверки →](./synthetic/README.md)**

**Возможности:**
- ✅ Тестирование UI/UX сценариев
- ✅ Проверка загрузки страниц
- ✅ Создание скриншотов
- ✅ Мониторинг форм и элементов

---

## 🚀 Быстрый старт

### 1️⃣ Получите API токен
Создайте токен в личном кабинете: [**app.pingera.ru**](https://app.pingera.ru) → [**"Настройки" → "API ключи"**](https://app.pingera.ru/settings/tokens)

### 2️⃣ Выберите способ использования

#### 🌐 Использование cURL

**Создание регулярной проверки:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @папка/check.json \
  https://api.pingera.ru/v1/checks
```

**Единоразовый запуск:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @папка/check.json \
  https://api.pingera.ru/v1/checks/execute
```

#### ⚡ Использование Pingera CLI

**Установка CLI:**
```bash
pip install pingera-cli
```

**Создание регулярной проверки:**
```bash
pngr checks create --from-file папка/check.json
# Можно использовать сокращенный флаг -f
pngr checks create -f папка/check.json
```

**Единоразовый запуск:**
```bash
pngr checks run custom --from-file папка/check.json
# Можно использовать сокращенный флаг -f
pngr checks run custom -f папка/check.json
```

**Поддержка удаленных файлов:**
```bash
# Загрузка файла конфигурации по URL
pngr checks create -f https://raw.githubusercontent.com/pingera/marketplace/refs/heads/main/multistep/simple.json
pngr checks run custom -f https://raw.githubusercontent.com/pingera/marketplace/refs/heads/main/synthetic/simple-screenshot.json
```

---

## 🔐 Работа с секретами

⚠️ **Важно:** Некоторые проверки требуют [**секреты**](https://docs.pingera.ru/checks/secrets) для аутентификации.

### Создание секретов:

**Через веб-интерфейс:**
1. [app.pingera.ru](https://app.pingera.ru) → "Секреты"
2. Нажмите "Создать секрет"

**Через CLI:**
```bash
pngr secrets create --name "SECRET_NAME" --value "SECRET_VALUE"
```

---

## 📝 Как добавить свой шаблон

### Структура файла

Ваш JSON-файл должен содержать **обязательный блок** `marketplace`:

```json
{
  "name": "Пример названия проверки",
  "type": "multistep", // или "synthetic"
  "interval": 300,
  "timeout": 30,
  "parameters": {
    // параметры проверки
  },
  "marketplace": {
    "name": "Понятное имя проверки",
    "description": "Подробное описание — для чего нужна проверка, кому будет полезна",
    "tags": ["тэг1", "тэг2", "мониторинг"],
    "secrets": true // если требуются секреты
  }
}
```

### 💡 Советы:
- 🏷️ **Используйте теги** — помогают пользователям находить ваши шаблоны
- 📝 **Подробное описание** — объясните, для чего нужна проверка
- 🔒 **Укажите secrets: true** — если проверка требует секреты

---

## 📊 Примеры шаблонов

### 🌐 Простая веб-проверка
```json
{
  "name": "Example Web Check",
  "type": "web",
  "url": "https://example.com",
  "interval": 300,
  "timeout": 30,
  "parameters": {
    "search_text": "Welcome",
    "http_request": {
      "method": "GET",
      "headers": {
        "User-Agent": "PingeraCLI/1.0"
      }
    }
  },
  "marketplace": {
    "tags": ["web", "basic"],
    "name": "Простая проверка веб-сайта",
    "description": "Запрашивает содержимое веб-сайта и ищет в ответе определенную строку"
  }
}
```

### 📸 Скриншот веб-сайта
```json
{
  "name": "Website Screenshot Monitor",
  "type": "synthetic", 
  "interval": 1800,
  "timeout": 30,
  "parameters": {
    "regions": ["RU, Moscow"],
    "pw_script": "const { test, expect } = require('@playwright/test');\n\ntest('website screenshot test', async ({ page }) => {\n  await page.goto('https://pingera.ru');\n  await page.waitForLoadState('load');\n  await page.waitForTimeout(2000);\n  await page.screenshot({ \n    path: 'website-screenshot.png', \n    fullPage: true \n  });\n  await expect(page).toHaveTitle(/Pingera/);\n  console.log('Screenshot captured successfully');\n});"
  },
  "marketplace": {
    "tags": ["screenshot", "visual-monitoring", "website"],
    "name": "Мониторинг скриншотов веб-сайта",
    "description": "Создает полноэкранные скриншоты веб-сайтов и проверяет загрузку страниц"
  }
}
```

---

## 🌍 Полезные ссылки

| Ресурс | Описание |
|--------|----------|
| 🏠 [**pingera.ru**](https://pingera.ru) | Главная страница платформы |
| 💼 [**app.pingera.ru**](https://app.pingera.ru) | Веб-приложение для управления |
| 📚 [**docs.pingera.ru**](https://docs.pingera.ru) | Документация и руководства |
| 🔗 [**API Docs**](https://docs.pingera.ru/api) | Справочник по API |
| ⚡ [**CLI Guide**](https://docs.pingera.ru/devs/cli) | Руководство по работе с CLI |
| 🔐 [**Секреты**](https://docs.pingera.ru/checks/secrets) | Работа с конфиденциальными данными |

---

<div align="center">

**🚀 Замониторь за 30 секунд с [Pingera](https://pingera.ru)!**

</div>
