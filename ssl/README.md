
# SSL/TLS проверки

🚀 **Эти скрипты предназначены для использования в [Платформе Pingera](https://pingera.ru)**

- **Приложение:** [app.pingera.ru](https://app.pingera.ru) - создание и управление проверками
- **Сайт:** [pingera.ru](https://pingera.ru) - общая информация о платформе
- **Документация:** [docs.pingera.ru](https://docs.pingera.ru) - подробная документация по API и CLI

## 🔒 О SSL/TLS проверках

Этот раздел содержит шаблоны SSL/TLS проверок, которые позволяют мониторить безопасность и настройки SSL сертификатов ваших сервисов.

**Возможности:**
- ✅ Проверка срока действия сертификатов
- ✅ Анализ настроек шифрования
- ✅ Выявление уязвимостей SSL/TLS
- ✅ Мониторинг цепочки сертификатов

## 📋 Содержание

- [Ежедневная проверка SSL сертификата](#simple)

---

### Ежедневная проверка SSL сертификата {#simple}

| Параметр | Значение |
|----------|----------|
| **Файл** | `simple.json` |
| **Тип проверки** | ssl |
| **Интервал** | 86400 сек |
| **Таймаут** | 30 сек |
| **Теги** | ssl, безопасность, сертификат |

**Описание:** Проверяет безопасность настроек SSL/TLS сертификата сервиса. Покажет шифры, уязвимости, настройки сертификатов.

#### Команды для использования

| Метод | Создание регулярной проверки | Единоразовый запуск |
|-------|------------------------------|---------------------|
| **cURL** | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @ssl/simple.json https://api.pingera.ru/v1/checks` | `curl -X POST -H "Authorization: ВАШ_ТОКЕН" -H "Content-Type: application/json" -d @ssl/simple.json https://api.pingera.ru/v1/checks/execute` |
| **Pingera CLI** | `pngr checks create --from-file ssl/simple.json` | `pngr checks run custom --from-file ssl/simple.json` |

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
