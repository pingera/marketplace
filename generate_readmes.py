
import json
import os
from pathlib import Path

def read_json_file(file_path):
    """Читает JSON файл и возвращает данные"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return None

def generate_toc(checks_data):
    """Генерирует оглавление с ссылками на проверки"""
    toc = "## 📋 Содержание\n\n"
    
    # Сортируем проверки по имени файла
    sorted_checks = sorted(checks_data.items())
    
    for filename, check_data in sorted_checks:
        marketplace = check_data.get('marketplace', {})
        name = marketplace.get('name', check_data.get('name', filename))
        # Создаем anchor link из имени файла
        anchor = filename.replace('.json', '').replace('-', '')
        toc += f"- [{name}](#{anchor})\n"
    
    toc += "\n"
    return toc

def generate_check_description(check_data, filename):
    """Генерирует описание проверки в компактном формате"""
    marketplace = check_data.get('marketplace', {})
    name = marketplace.get('name', check_data.get('name', filename))
    description = marketplace.get('description', 'Описание отсутствует')
    tags = marketplace.get('tags', [])
    secrets_required = marketplace.get('secrets', False)
    
    check_type = check_data.get('type', 'unknown')
    interval = check_data.get('interval', 'не указан')
    timeout = check_data.get('timeout', 'не указан')
    
    # Создаем anchor из имени файла
    anchor = filename.replace('.json', '').replace('-', '')
    
    result = f"### {name} {{#{anchor}}}\n\n"
    
    # Основная информация в таблице
    result += "| Параметр | Значение |\n"
    result += "|----------|----------|\n"
    result += f"| **Файл** | `{filename}` |\n"
    result += f"| **Тип проверки** | {check_type} |\n"
    result += f"| **Интервал** | {interval} сек |\n"
    result += f"| **Таймаут** | {timeout} сек |\n"
    
    if tags:
        result += f"| **Теги** | {', '.join(tags)} |\n"
    
    if secrets_required:
        result += f"| **Требует секреты** | ⚠️ Да |\n"
    
    result += "\n"
    result += f"**Описание:** {description}\n\n"
    
    if secrets_required:
        result += "⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.\n\n"
    
    # Команды в компактной таблице
    result += "#### Команды для использования\n\n"
    result += "| Метод | Создание регулярной проверки | Единоразовый запуск |\n"
    result += "|-------|------------------------------|---------------------|\n"
    
    # cURL команды
    curl_create = f"`curl -X POST -H \"Authorization: ВАШ_ТОКЕН\" -H \"Content-Type: application/json\" -d @{check_data.get('type', 'multistep')}/{filename} https://api.pingera.ru/v1/checks`"
    curl_execute = f"`curl -X POST -H \"Authorization: ВАШ_ТОКЕН\" -H \"Content-Type: application/json\" -d @{check_data.get('type', 'multistep')}/{filename} https://api.pingera.ru/v1/checks/execute`"
    
    result += f"| **cURL** | {curl_create} | {curl_execute} |\n"
    
    # CLI команды
    cli_create = f"`pngr checks create --from-file {check_data.get('type', 'multistep')}/{filename}`"
    cli_execute = f"`pngr checks run custom --from-file {check_data.get('type', 'multistep')}/{filename}`"
    
    result += f"| **Pingera CLI** | {cli_create} | {cli_execute} |\n"
    
    result += "\n"
    
    return result

def generate_readme_content(folder_name, checks_data):
    """Генерирует содержимое README файла"""
    folder_display_name = "Многошаговые проверки" if folder_name == "multistep" else "Синтетические проверки"
    
    content = f"# {folder_display_name}\n\n"
    
    # Информация о платформе
    content += "🚀 **Эти скрипты предназначены для использования в [Платформе Pingera](https://pingera.ru)**\n\n"
    content += "- **Приложение:** [app.pingera.ru](https://app.pingera.ru) - создание и управление проверками\n"
    content += "- **Сайт:** [pingera.ru](https://pingera.ru) - общая информация о платформе\n"
    content += "- **Документация:** [docs.pingera.ru](https://docs.pingera.ru) - подробная документация по API и CLI\n\n"
    
    if folder_name == "multistep":
        content += "## 🔄 О многошаговых проверках\n\n"
        content += "Этот раздел содержит шаблоны многошаговых проверок (multistep checks), которые используют Playwright для выполнения сложных сценариев тестирования API и веб-приложений.\n\n"
        content += "**Возможности:**\n"
        content += "- ✅ Выполнение последовательности HTTP-запросов\n"
        content += "- ✅ Тестирование API endpoints\n"
        content += "- ✅ Проверка сложных бизнес-процессов\n"
        content += "- ✅ Использование секретов для аутентификации\n\n"
    else:
        content += "## 🎭 О синтетических проверках\n\n"
        content += "Этот раздел содержит шаблоны синтетических проверок (synthetic checks), которые используют Playwright для тестирования веб-интерфейсов и пользовательских сценариев.\n\n"
        content += "**Возможности:**\n"
        content += "- ✅ Тестирование пользовательских сценариев\n"
        content += "- ✅ Проверка загрузки страниц\n"
        content += "- ✅ Создание скриншотов для визуального мониторинга\n"
        content += "- ✅ Проверка работы форм и элементов интерфейса\n\n"
    
    # Добавляем оглавление
    content += generate_toc(checks_data)
    
    content += "---\n\n"
    
    # Сортируем проверки по имени файла
    sorted_checks = sorted(checks_data.items())
    
    for filename, check_data in sorted_checks:
        content += generate_check_description(check_data, filename)
    
    content += "---\n\n"
    content += "## 📚 Справочная информация\n\n"
    
    content += "### 🔑 Получение API токена\n\n"
    content += "Для работы с API вам понадобится **API токен**. Создайте его в личном кабинете:\n"
    content += "1. Перейдите в [app.pingera.ru](https://app.pingera.ru)\n"
    content += "2. Откройте раздел [**\"Настройки\" → \"API ключи\"**](https://app.pingera.ru/settings/tokens)\n"
    content += "3. Нажмите \"Создать новый токен\"\n\n"
    
    content += "### 🔐 Работа с секретами\n\n"
    content += "Некоторые проверки требуют использования [Секретов](https://docs.pingera.ru/checks/secrets). "
    content += "Создайте их заранее через:\n\n"
    content += "**Веб-интерфейс:**\n"
    content += "1. [app.pingera.ru](https://app.pingera.ru) → \"Секреты\"\n"
    content += "2. Нажмите \"Создать секрет\"\n\n"
    content += "**CLI:**\n"
    content += "```bash\n"
    content += "pngr secrets create --name \"SECRET_NAME\" --value \"SECRET_VALUE\"\n"
    content += "```\n\n"
    
    content += "### 🌍 Регионы выполнения\n\n"
    content += "Большинство проверок настроены для выполнения из следующих регионов:\n\n"
    content += "| Регион | Описание |\n"
    content += "|--------|----------|\n"
    content += "| `RU, Moscow` | Москва, Россия |\n"
    content += "| `EU, West` | Западная Европа |\n"
    content += "| `US, East coast` | Восточное побережье США |\n"
    content += "| `IN, Mumbai` | Мумбаи, Индия |\n"
    content += "| `QA, Doha` | Доха, Катар |\n\n"
    
    content += "Вы можете изменить регионы в конфигурации проверки перед её созданием.\n\n"
    
    content += "### 📖 Дополнительные ресурсы\n\n"
    content += "- [Документация по API](https://docs.pingera.ru/api)\n"
    content += "- [Руководство по CLI](https://docs.pingera.ru/devs/cli)\n"
    content += "- [Примеры проверок](https://docs.pingera.ru/checks)\n"
    content += "- [Работа с секретами](https://docs.pingera.ru/checks/secrets)\n\n"
    
    return content

def main():
    """Основная функция"""
    folders = ['multistep', 'synthetic']
    
    for folder in folders:
        if not os.path.exists(folder):
            print(f"Папка {folder} не найдена")
            continue
        
        checks_data = {}
        
        # Читаем все JSON файлы в папке
        for file_path in Path(folder).glob('*.json'):
            check_data = read_json_file(file_path)
            if check_data:
                checks_data[file_path.name] = check_data
        
        if not checks_data:
            print(f"В папке {folder} не найдено JSON файлов")
            continue
        
        # Генерируем содержимое README
        readme_content = generate_readme_content(folder, checks_data)
        
        # Записываем README файл
        readme_path = os.path.join(folder, 'README.md')
        try:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            print(f"✅ Создан файл {readme_path}")
        except Exception as e:
            print(f"❌ Ошибка при создании файла {readme_path}: {e}")

if __name__ == "__main__":
    main()
