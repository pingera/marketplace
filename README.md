# Маркетплейс Pingera: Шаблоны проверок и Статус Страниц

Этот репозиторий содержит **идеи и готовые шаблоны** для создания проверок и Статус Страниц на платформе [Pingera](https://pingera.ru).

Вы можете поделиться своими идеями и шаблонами, отправив **Pull Request**.

## Как начать

Для работы с API вам понадобится **API токен**. Вы можете создать его в личном кабинете, в разделе [**"Настройки" -> "API ключи"**](https://app.pingera.ru/settings/tokens). 

## Создание регулярной проверки

Вы можете создать проверку, используя утилиту **`cURL`** или официальный [**Pingera CLI (pngr)**](https://docs.pingera.ru/devs/cli).

### Использование cURL

Чтобы создать проверку, выполните следующую команду в терминале, заменив `ВАШ_ТОКЕН` на ваш реальный API ключ:

```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @somedir/check.json \
  [https://api.pingera.ru/v1/checks](https://api.pingera.ru/v1/checks)
```

### Использование Pingera CLI
Если вы предпочитаете использовать CLI, команда будет более лаконичной:

```bash
pngr checks create --from-file somedir/check.json
```

## Запуск проверки (on-demand)

Вы также можете запустить проверку из маркетплейса единоразово. Это удобно для тестирования или интеграции с CI/CD.

### Использование cURL

```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @somedir/check.json \
  [https://api.pingera.ru/v1/checks/execute](https://api.pingera.ru/v1/checks/execute)
```

### Использование Pingera CLI

```bash
pngr checks run custom --from-file somedir/check.json
```

## Примечание о секретах
Для некоторых проверок может потребоваться использование [Секретов](https://docs.pingera.ru/checks/secrets). Вы можете создать их заранее или добавить позже через веб-интерфейс, API или CLI.

## Как добавить свой шаблон проверки
Чтобы добавить свой шаблон, просто отправьте Pull Request с файлом в формате JSON. В этом файле должны быть указаны все необходимые поля для проверки, как описано в документации по API.

### Обязательные поля для маркетплейса
Помимо стандартных полей, ваш JSON-файл должен содержать блок marketplace, чтобы информация о шаблоне корректно отображалась на сайте и в личном кабинете.

```json
{
  "name": "Пример названия проверки",
  ...
  "marketplace": {
    "name": "Имя проверки",
    "description": "Описание проверки — для чего она нужна, кому будет полезна и прочее.",
    "tags": ["тэг1", "тэг2", "мониторинг", "веб-сайт"]
  }
}
```
**Совет:** Используйте теги, чтобы пользователям было легче найти ваш шаблон. 

### Примеры

#### Обычная проверка веб сайта
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
    "name": "Простая проверка веб-сайта с поиском строки в ответе",
    "description": "Запрашивает содержимое веб-сайта и ищет в ответе определенную строку",
  }
}
```

#### Простая playwright проверка со скриншотом
```json

{
  "name": "Website Screenshot Monitor",
  "type": "synthetic", 
  "interval": 1800,
  "timeout": 30,
  "parameters": {
    "regions": ["RU, Moscow"],
    "pw_script": "const { test, expect } = require('@playwright/test');\n\ntest('website screenshot test', async ({ page }) => {\n  // Navigate to the website\n  await page.goto('https://pingera.ru');\n  \n  // Wait for the page to fully load\n  await page.waitForLoadState('load');\n  \n  // Additional wait to ensure all dynamic content is loaded\n  await page.waitForTimeout(2000);\n  \n  // Take a full page screenshot\n  await page.screenshot({ \n    path: 'website-screenshot.png', \n    fullPage: true \n  });\n  \n  // Verify the page loaded successfully\n  await expect(page).toHaveTitle(/Example/);\n  \n  // Check for key elements on the page\n  await expect(page.locator('h1')).toBeVisible();\n  \n  console.log('Screenshot captured and page verified successfully');\n});",
  },
  "marketplace": {
    "tags": ["screenshot", "visual-monitoring", "website-monitoring"],
    "name": "Website Screenshot Monitor",
    "description": "Captures full-page screenshots of websites and verifies page loading",
  }
}
```
