# Синтетические проверки

🚀 **Эти скрипты предназначены для использования в [Платформе Pingera](https://pingera.ru)**

- **Приложение:** [app.pingera.ru](https://app.pingera.ru) - создание и управление проверками
- **Сайт:** [pingera.ru](https://pingera.ru) - общая информация о платформе
- **Документация:** [docs.pingera.ru](https://docs.pingera.ru) - подробная документация по API и CLI

## 🎭 О синтетических проверках

Этот раздел содержит шаблоны синтетических проверок (synthetic checks), которые используют Playwright для тестирования веб-интерфейсов и пользовательских сценариев.

**Возможности:**
- ✅ Тестирование пользовательских сценариев
- ✅ Проверка загрузки страниц
- ✅ Создание скриншотов для визуального мониторинга
- ✅ Проверка работы форм и элементов интерфейса

## 📋 Содержание

- [Проверка битых изображений](#checkbrokenpics)
- [Проверка ключевых элементов на странице](#checkpageelements)
- [Проверка скорости загрузки страницы](#checkpageloadtime)
- [Мониторинг поиска на сайте](#checksearchonweb)
- [Мониторинг формы входа](#loginform)
- [Простой мониторинг скриншотов](#simplescreenshot)
- [Мониторинг динамического контента](#waitfordynamiccontent)

---

### Проверка битых изображений {#checkbrokenpics}

| Параметр | Значение |
|----------|----------|
| **Файл** | `check-broken-pics.json` |
| **Тип проверки** | synthetic |
| **Интервал** | 3600 сек |
| **Таймаут** | 30 сек |
| **Теги** | изображения, ошибки, контент, битые-ссылки |

**Описание:** Сканирует веб-страницу на наличие битых или недоступных изображений.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/check-broken-pics.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/check-broken-pics.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file synthetic/check-broken-pics.json` | `pngr checks run custom --from-file synthetic/check-broken-pics.json` |

### Проверка ключевых элементов на странице {#checkpageelements}

| Параметр | Значение |
|----------|----------|
| **Файл** | `check-page-elements.json` |
| **Тип проверки** | synthetic |
| **Интервал** | 120 сек |
| **Таймаут** | 20 сек |
| **Теги** | доступность, элементы-страницы, ui-monitoring, веб-сайт |

**Описание:** Проверяет наличие и видимость ключевых элементов на веб-странице.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/check-page-elements.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/check-page-elements.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file synthetic/check-page-elements.json` | `pngr checks run custom --from-file synthetic/check-page-elements.json` |

### Проверка скорости загрузки страницы {#checkpageloadtime}

| Параметр | Значение |
|----------|----------|
| **Файл** | `check-page-load-time.json` |
| **Тип проверки** | synthetic |
| **Интервал** | 1800 сек |
| **Таймаут** | 30 сек |
| **Теги** | производительность, скорость-загрузки, время-ответа, метрики |

**Описание:** Измеряет время загрузки страницы и проверяет, что оно не превышает заданный лимит.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/check-page-load-time.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/check-page-load-time.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file synthetic/check-page-load-time.json` | `pngr checks run custom --from-file synthetic/check-page-load-time.json` |

### Мониторинг поиска на сайте {#checksearchonweb}

| Параметр | Значение |
|----------|----------|
| **Файл** | `check-search-on-web.json` |
| **Тип проверки** | synthetic |
| **Интервал** | 900 сек |
| **Таймаут** | 30 сек |
| **Теги** | поиск, пользовательский-путь, функциональность, веб-приложение |

**Описание:** Имитирует поиск на сайте и проверяет, что результаты отображаются.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/check-search-on-web.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/check-search-on-web.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file synthetic/check-search-on-web.json` | `pngr checks run custom --from-file synthetic/check-search-on-web.json` |

### Мониторинг формы входа {#loginform}

| Параметр | Значение |
|----------|----------|
| **Файл** | `login-form.json` |
| **Тип проверки** | synthetic |
| **Интервал** | 300 сек |
| **Таймаут** | 30 сек |
| **Теги** | авторизация, форма-входа, доступность, безопасность |
| **Требует секреты** | ⚠️ Да |

**Описание:** Имитирует процесс входа пользователя, используя Playwright, и проверяет успешную авторизацию.

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/login-form.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/login-form.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file synthetic/login-form.json` | `pngr checks run custom --from-file synthetic/login-form.json` |

### Простой мониторинг скриншотов {#simplescreenshot}

| Параметр | Значение |
|----------|----------|
| **Файл** | `simple-screenshot.json` |
| **Тип проверки** | synthetic |
| **Интервал** | 1800 сек |
| **Таймаут** | 30 сек |
| **Теги** | скриншот, визуальный-мониторинг, доступность |

**Описание:** Самая простая проверка, которая делает полностраничный скриншот сайта.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/simple-screenshot.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/simple-screenshot.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file synthetic/simple-screenshot.json` | `pngr checks run custom --from-file synthetic/simple-screenshot.json` |

### Мониторинг динамического контента {#waitfordynamiccontent}

| Параметр | Значение |
|----------|----------|
| **Файл** | `wait-for-dynamic-content.json` |
| **Тип проверки** | synthetic |
| **Интервал** | 300 сек |
| **Таймаут** | 30 сек |
| **Теги** | динамический-контент, ajax, react, vue |

**Описание:** Проверяет, что определённый элемент, подгружаемый асинхронно, успешно появился на странице.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/wait-for-dynamic-content.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @synthetic/wait-for-dynamic-content.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file synthetic/wait-for-dynamic-content.json` | `pngr checks run custom --from-file synthetic/wait-for-dynamic-content.json` |

---

## 📚 Справочная информация

### 🔑 Получение API токена

Для работы с API вам понадобится **API токен**. Создайте его в личном кабинете:
1. Перейдите в [app.pingera.ru](https://app.pingera.ru)
2. Откройте раздел [**"Настройки" → "API ключи"**](https://app.pingera.ru/settings/tokens)
3. Нажмите "Создать новый токен"

### 🔐 Работа с секретами

Некоторые проверки требуют использования [Секретов](https://docs.pingera.ru/checks/secrets). Создайте их заранее через:

**Веб-интерфейс:**
1. [app.pingera.ru](https://app.pingera.ru) → "Секреты"
2. Нажмите "Создать секрет"

**CLI:**
```bash
pngr secrets create --name "SECRET_NAME" --value "SECRET_VALUE"
```

### 🌍 Регионы выполнения

Большинство проверок настроены для выполнения из следующих регионов:

| Регион | Описание |
|--------|----------|
| `RU, Moscow` | Москва, Россия |
| `EU, West` | Западная Европа |
| `US, East coast` | Восточное побережье США |
| `IN, Mumbai` | Мумбаи, Индия |
| `QA, Doha` | Доха, Катар |

Вы можете изменить регионы в конфигурации проверки перед её созданием.

### 📖 Дополнительные ресурсы

- [Документация по API](https://docs.pingera.ru/api)
- [Руководство по CLI](https://docs.pingera.ru/devs/cli)
- [Примеры проверок](https://docs.pingera.ru/checks)
- [Работа с секретами](https://docs.pingera.ru/checks/secrets)

