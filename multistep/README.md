# Многошаговые проверки

Этот раздел содержит шаблоны многошаговых проверок (multistep checks), которые используют Playwright для выполнения сложных сценариев тестирования API и веб-приложений.

Многошаговые проверки позволяют:
- Выполнять последовательности HTTP-запросов
- Тестировать API endpoints
- Проверять сложные бизнес-процессы
- Использовать секреты для аутентификации

## Доступные проверки

### Тестирование API-токенов

**Файл:** `check-api-tokens.json`

**Описание:** Создает, проверяет и удаляет API-токен для мониторинга работоспособности API аутентификации. Требует наличия секретов.

**Тип проверки:** multistep

**Интервал:** 1800 секунд

**Таймаут:** 30 секунд

**Теги:** api, crud, токен, безопасность, пользователи

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

**Использование с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @multistep/check-api-tokens.json \
  https://api.pingera.ru/v1/checks
```

**Использование с Pingera CLI:**
```bash
pngr checks create --from-file multistep/check-api-tokens.json
```

**Единоразовый запуск с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @multistep/check-api-tokens.json \
  https://api.pingera.ru/v1/checks/execute
```

**Единоразовый запуск с Pingera CLI:**
```bash
pngr checks run custom --from-file multistep/check-api-tokens.json
```

### Тестирование ролей пользователей

**Файл:** `check-roles.json`

**Описание:** Тестирует приглашение нового пользователя и изменение его роли. Требует прав администратора и наличия секретов.

**Тип проверки:** multistep

**Интервал:** 86400 секунд

**Таймаут:** 30 секунд

**Теги:** пользователи, админ, права-доступа, роли, бизнес-процесс

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

**Использование с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @multistep/check-roles.json \
  https://api.pingera.ru/v1/checks
```

**Использование с Pingera CLI:**
```bash
pngr checks create --from-file multistep/check-roles.json
```

**Единоразовый запуск с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @multistep/check-roles.json \
  https://api.pingera.ru/v1/checks/execute
```

**Единоразовый запуск с Pingera CLI:**
```bash
pngr checks run custom --from-file multistep/check-roles.json
```

### Проверка Heartbeat API

**Файл:** `heartbeart.json`

**Описание:** Отправляет пинг на Heartbeat-эндпоинт и проверяет, что статус чека меняется на 'up'. Требует наличия секретов.

**Тип проверки:** multistep

**Интервал:** 300 секунд

**Таймаут:** 30 секунд

**Теги:** heartbeat, api, cron, задачи-по-расписанию, доступность

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

**Использование с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @multistep/heartbeart.json \
  https://api.pingera.ru/v1/checks
```

**Использование с Pingera CLI:**
```bash
pngr checks create --from-file multistep/heartbeart.json
```

**Единоразовый запуск с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @multistep/heartbeart.json \
  https://api.pingera.ru/v1/checks/execute
```

**Единоразовый запуск с Pingera CLI:**
```bash
pngr checks run custom --from-file multistep/heartbeart.json
```

### Жизненный цикл инцидента

**Файл:** `incident-mgmt.json`

**Описание:** Проверяет создание, обновление и удаление инцидента на статус-странице. Требует наличия секретов.

**Тип проверки:** multistep

**Интервал:** 900 секунд

**Таймаут:** 30 секунд

**Теги:** инциденты, статус-страница, управление-инцидентами, api

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

**Использование с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @multistep/incident-mgmt.json \
  https://api.pingera.ru/v1/checks
```

**Использование с Pingera CLI:**
```bash
pngr checks create --from-file multistep/incident-mgmt.json
```

**Единоразовый запуск с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @multistep/incident-mgmt.json \
  https://api.pingera.ru/v1/checks/execute
```

**Единоразовый запуск с Pingera CLI:**
```bash
pngr checks run custom --from-file multistep/incident-mgmt.json
```

### Проверка on-demand с секретами

**Файл:** `ondemand-secret.json`

**Описание:** Запускает разовую проверку, которая использует секреты организации, чтобы убедиться в их корректной передаче в Playwright скрипт. Требует наличия секретов.

**Тип проверки:** multistep

**Интервал:** 3600 секунд

**Таймаут:** 30 секунд

**Теги:** секреты, on-demand, безопасность, api

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

**Использование с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @multistep/ondemand-secret.json \
  https://api.pingera.ru/v1/checks
```

**Использование с Pingera CLI:**
```bash
pngr checks create --from-file multistep/ondemand-secret.json
```

**Единоразовый запуск с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @multistep/ondemand-secret.json \
  https://api.pingera.ru/v1/checks/execute
```

**Единоразовый запуск с Pingera CLI:**
```bash
pngr checks run custom --from-file multistep/ondemand-secret.json
```

### Простейший GET API-мониторинг

**Файл:** `simple.json`

**Описание:** Отправляет простой GET-запрос к API-эндпоинту и проверяет, что он возвращает код 200. Использует переменную окружения для URL.

**Тип проверки:** multistep

**Интервал:** 60 секунд

**Таймаут:** 15 секунд

**Теги:** api, доступность, простота, http

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

**Использование с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @multistep/simple.json \
  https://api.pingera.ru/v1/checks
```

**Использование с Pingera CLI:**
```bash
pngr checks create --from-file multistep/simple.json
```

**Единоразовый запуск с cURL:**
```bash
curl -X POST \
  -H "Authorization: ВАШ_ТОКЕН" \
  -H "Content-Type: application/json" \
  -d @multistep/simple.json \
  https://api.pingera.ru/v1/checks/execute
```

**Единоразовый запуск с Pingera CLI:**
```bash
pngr checks run custom --from-file multistep/simple.json
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

