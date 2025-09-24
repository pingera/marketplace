# Синтетические проверки

Этот раздел содержит шаблоны синтетических проверок (synthetic checks), которые используют Playwright для тестирования веб-интерфейсов и пользовательских сценариев.

Синтетические проверки позволяют:
- Тестировать пользовательские сценарии
- Проверять загрузку страниц
- Делать скриншоты для визуального мониторинга
- Проверять работу форм и элементов интерфейса

## Доступные проверки

### Проверка битых изображений

**Файл:** `check-broken-pics.json`

**Описание:** Сканирует веб-страницу на наличие битых или недоступных изображений.

**Тип проверки:** synthetic

**Интервал:** 3600 секунд

**Таймаут:** 30 секунд

**Теги:** изображения, ошибки, контент, битые-ссылки

**Использование с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/check-broken-pics.json \
  https://api.pingera.ru/v1/checks
```

**Использование с Pingera CLI:**
```bash
pngr checks create --from-file synthetic/check-broken-pics.json
```

**Единоразовый запуск с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/check-broken-pics.json \
  https://api.pingera.ru/v1/checks/execute
```

**Единоразовый запуск с Pingera CLI:**
```bash
pngr checks run custom --from-file synthetic/check-broken-pics.json
```

### Проверка ключевых элементов на странице

**Файл:** `check-page-elements.json`

**Описание:** Проверяет наличие и видимость ключевых элементов на веб-странице.

**Тип проверки:** synthetic

**Интервал:** 120 секунд

**Таймаут:** 20 секунд

**Теги:** доступность, элементы-страницы, ui-monitoring, веб-сайт

**Использование с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/check-page-elements.json \
  https://api.pingera.ru/v1/checks
```

**Использование с Pingera CLI:**
```bash
pngr checks create --from-file synthetic/check-page-elements.json
```

**Единоразовый запуск с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/check-page-elements.json \
  https://api.pingera.ru/v1/checks/execute
```

**Единоразовый запуск с Pingera CLI:**
```bash
pngr checks run custom --from-file synthetic/check-page-elements.json
```

### Проверка скорости загрузки страницы

**Файл:** `check-page-load-time.json`

**Описание:** Измеряет время загрузки страницы и проверяет, что оно не превышает заданный лимит.

**Тип проверки:** synthetic

**Интервал:** 1800 секунд

**Таймаут:** 30 секунд

**Теги:** производительность, скорость-загрузки, время-ответа, метрики

**Использование с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/check-page-load-time.json \
  https://api.pingera.ru/v1/checks
```

**Использование с Pingera CLI:**
```bash
pngr checks create --from-file synthetic/check-page-load-time.json
```

**Единоразовый запуск с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/check-page-load-time.json \
  https://api.pingera.ru/v1/checks/execute
```

**Единоразовый запуск с Pingera CLI:**
```bash
pngr checks run custom --from-file synthetic/check-page-load-time.json
```

### Мониторинг поиска на сайте

**Файл:** `check-search-on-web.json`

**Описание:** Имитирует поиск на сайте и проверяет, что результаты отображаются.

**Тип проверки:** synthetic

**Интервал:** 900 секунд

**Таймаут:** 30 секунд

**Теги:** поиск, пользовательский-путь, функциональность, веб-приложение

**Использование с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/check-search-on-web.json \
  https://api.pingera.ru/v1/checks
```

**Использование с Pingera CLI:**
```bash
pngr checks create --from-file synthetic/check-search-on-web.json
```

**Единоразовый запуск с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/check-search-on-web.json \
  https://api.pingera.ru/v1/checks/execute
```

**Единоразовый запуск с Pingera CLI:**
```bash
pngr checks run custom --from-file synthetic/check-search-on-web.json
```

### Мониторинг формы входа

**Файл:** `login-form.json`

**Описание:** Имитирует процесс входа пользователя, используя Playwright, и проверяет успешную авторизацию.

**Тип проверки:** synthetic

**Интервал:** 300 секунд

**Таймаут:** 30 секунд

**Теги:** авторизация, форма-входа, доступность, безопасность

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

**Использование с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/login-form.json \
  https://api.pingera.ru/v1/checks
```

**Использование с Pingera CLI:**
```bash
pngr checks create --from-file synthetic/login-form.json
```

**Единоразовый запуск с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/login-form.json \
  https://api.pingera.ru/v1/checks/execute
```

**Единоразовый запуск с Pingera CLI:**
```bash
pngr checks run custom --from-file synthetic/login-form.json
```

### Простой мониторинг скриншотов

**Файл:** `simple-screenshot.json`

**Описание:** Самая простая проверка, которая делает полностраничный скриншот сайта.

**Тип проверки:** synthetic

**Интервал:** 1800 секунд

**Таймаут:** 30 секунд

**Теги:** скриншот, визуальный-мониторинг, доступность

**Использование с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/simple-screenshot.json \
  https://api.pingera.ru/v1/checks
```

**Использование с Pingera CLI:**
```bash
pngr checks create --from-file synthetic/simple-screenshot.json
```

**Единоразовый запуск с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/simple-screenshot.json \
  https://api.pingera.ru/v1/checks/execute
```

**Единоразовый запуск с Pingera CLI:**
```bash
pngr checks run custom --from-file synthetic/simple-screenshot.json
```

### Мониторинг динамического контента

**Файл:** `wait-for-dynamic-content.json`

**Описание:** Проверяет, что определённый элемент, подгружаемый асинхронно, успешно появился на странице.

**Тип проверки:** synthetic

**Интервал:** 300 секунд

**Таймаут:** 30 секунд

**Теги:** динамический-контент, ajax, react, vue

**Использование с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/wait-for-dynamic-content.json \
  https://api.pingera.ru/v1/checks
```

**Использование с Pingera CLI:**
```bash
pngr checks create --from-file synthetic/wait-for-dynamic-content.json
```

**Единоразовый запуск с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @synthetic/wait-for-dynamic-content.json \
  https://api.pingera.ru/v1/checks/execute
```

**Единоразовый запуск с Pingera CLI:**
```bash
pngr checks run custom --from-file synthetic/wait-for-dynamic-content.json
```

## Общая информация

### Получение API токена

Для работы с API вам понадобится **API токен**. Вы можете создать его в личном кабинете, в разделе [**"Настройки" -> "API ключи"**](https://app.pingera.ru/settings/tokens).

### Работа с секретами

Некоторые проверки требуют использования [Секретов](https://docs.pingera.ru/checks/secrets). Вы можете создать их заранее через веб-интерфейс, API или CLI:

```bash
pngr secrets create --name "SECRET_NAME" --value "SECRET_VALUE"
```

### Регионы выполнения

Большинство проверок настроены для выполнения из следующих регионов:
- `RU, Moscow` - Москва, Россия
- `EU, West` - Западная Европа
- `US, East coast` - Восточное побережье США
- `IN, Mumbai` - Мумбаи, Индия
- `QA, Doha` - Доха, Катар

Вы можете изменить регионы в конфигурации проверки перед её созданием.

