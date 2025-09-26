# Многошаговые проверки

🚀 **Эти скрипты предназначены для использования в [Платформе Pingera](https://pingera.ru)**

- **Приложение:** [app.pingera.ru](https://app.pingera.ru) - создание и управление проверками
- **Сайт:** [pingera.ru](https://pingera.ru) - общая информация о платформе
- **Документация:** [docs.pingera.ru](https://docs.pingera.ru) - подробная документация по API и CLI

## 🔄 О многошаговых проверках

Этот раздел содержит шаблоны многошаговых проверок (multistep checks), которые используют Playwright для выполнения сложных сценариев тестирования API и веб-приложений.

**Возможности:**
- ✅ Выполнение последовательности HTTP-запросов
- ✅ Тестирование API endpoints
- ✅ Проверка сложных бизнес-процессов
- ✅ Использование секретов для аутентификации

## 📋 Содержание

- [Тестирование API-токенов](#checkapitokens)
- [Тестирование ролей пользователей](#checkroles)
- [Проверка Heartbeat API](#heartbeart)
- [Жизненный цикл инцидента](#incidentmgmt)
- [Проверка on-demand с секретами](#ondemandsecret)
- [Простейший GET API-мониторинг](#simple)

---

### Тестирование API-токенов {#checkapitokens}

| Параметр | Значение |
|----------|----------|
| **Файл** | `check-api-tokens.json` |
| **Тип проверки** | multistep |
| **Интервал** | 1800 сек |
| **Таймаут** | 30 сек |
| **Теги** | api, crud, токен, безопасность, пользователи |
| **Требует секреты** | ⚠️ Да |

**Описание:** Создает, проверяет и удаляет API-токен для мониторинга работоспособности API аутентификации. Требует наличия секретов.

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @multistep/check-api-tokens.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @multistep/check-api-tokens.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file multistep/check-api-tokens.json` | `pngr checks run custom --from-file multistep/check-api-tokens.json` |

### Тестирование ролей пользователей {#checkroles}

| Параметр | Значение |
|----------|----------|
| **Файл** | `check-roles.json` |
| **Тип проверки** | multistep |
| **Интервал** | 86400 сек |
| **Таймаут** | 30 сек |
| **Теги** | пользователи, админ, права-доступа, роли, бизнес-процесс |
| **Требует секреты** | ⚠️ Да |

**Описание:** Тестирует приглашение нового пользователя и изменение его роли. Требует прав администратора и наличия секретов.

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @multistep/check-roles.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @multistep/check-roles.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file multistep/check-roles.json` | `pngr checks run custom --from-file multistep/check-roles.json` |

### Проверка Heartbeat API {#heartbeart}

| Параметр | Значение |
|----------|----------|
| **Файл** | `heartbeart.json` |
| **Тип проверки** | multistep |
| **Интервал** | 300 сек |
| **Таймаут** | 30 сек |
| **Теги** | heartbeat, api, cron, задачи-по-расписанию, доступность |
| **Требует секреты** | ⚠️ Да |

**Описание:** Отправляет пинг на Heartbeat-эндпоинт и проверяет, что статус чека меняется на 'up'. Требует наличия секретов.

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @multistep/heartbeart.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @multistep/heartbeart.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file multistep/heartbeart.json` | `pngr checks run custom --from-file multistep/heartbeart.json` |

### Жизненный цикл инцидента {#incidentmgmt}

| Параметр | Значение |
|----------|----------|
| **Файл** | `incident-mgmt.json` |
| **Тип проверки** | multistep |
| **Интервал** | 900 сек |
| **Таймаут** | 30 сек |
| **Теги** | инциденты, статус-страница, управление-инцидентами, api |
| **Требует секреты** | ⚠️ Да |

**Описание:** Проверяет создание, обновление и удаление инцидента на статус-странице. Требует наличия секретов.

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @multistep/incident-mgmt.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @multistep/incident-mgmt.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file multistep/incident-mgmt.json` | `pngr checks run custom --from-file multistep/incident-mgmt.json` |

### Проверка on-demand с секретами {#ondemandsecret}

| Параметр | Значение |
|----------|----------|
| **Файл** | `ondemand-secret.json` |
| **Тип проверки** | multistep |
| **Интервал** | 3600 сек |
| **Таймаут** | 30 сек |
| **Теги** | секреты, on-demand, безопасность, api |
| **Требует секреты** | ⚠️ Да |

**Описание:** Запускает разовую проверку, которая использует секреты организации, чтобы убедиться в их корректной передаче в Playwright скрипт. Требует наличия секретов.

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @multistep/ondemand-secret.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @multistep/ondemand-secret.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file multistep/ondemand-secret.json` | `pngr checks run custom --from-file multistep/ondemand-secret.json` |

### Простейший GET API-мониторинг {#simple}

| Параметр | Значение |
|----------|----------|
| **Файл** | `simple.json` |
| **Тип проверки** | multistep |
| **Интервал** | 60 сек |
| **Таймаут** | 15 сек |
| **Теги** | api, доступность, простота, http |
| **Требует секреты** | ⚠️ Да |

**Описание:** Отправляет простой GET-запрос к API-эндпоинту и проверяет, что он возвращает код 200. Использует переменную окружения для URL.

⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @multistep/simple.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @multistep/simple.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file multistep/simple.json` | `pngr checks run custom --from-file multistep/simple.json` |

---

## 📚 Справочная информация

### 🔑 Получение API токена

Для работы с API вам понадобится **API токен**. Создайте его в личном кабинете:
1. Перейдите в [app.pingera.ru](https://app.pingera.ru)
2. Откройте раздел [**"Настройки" → "API ключи"**](https://app.pingera.ru/settings/tokens)
3. Нажмите "Создать новый токен"

### ⚡ Дополнительные возможности CLI

**Сокращенные флаги:** Вы можете использовать как `--from-file`, так и `-f`:
```bash
pngr checks create -f папка/check.json
pngr checks run custom -f папка/check.json
```

**Удаленные файлы:** CLI поддерживает загрузку файлов по URL:
```bash
pngr checks create -f https://raw.githubusercontent.com/pingera/marketplace/refs/heads/main/multistep/simple.json
pngr checks run custom -f https://raw.githubusercontent.com/pingera/marketplace/refs/heads/main/synthetic/simple-screenshot.json
```

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

- [Документация по API](https://docs.pingera.ru/api/overview)
- [Руководство по CLI](https://docs.pingera.ru/devs/cli)
- [Примеры проверок](https://docs.pingera.ru/checks/overview)
- [Работа с секретами](https://docs.pingera.ru/checks/secrets)

