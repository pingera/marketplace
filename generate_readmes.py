
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

def generate_check_description(check_data, filename):
    """Генерирует описание проверки"""
    marketplace = check_data.get('marketplace', {})
    name = marketplace.get('name', check_data.get('name', filename))
    description = marketplace.get('description', 'Описание отсутствует')
    tags = marketplace.get('tags', [])
    secrets_required = marketplace.get('secrets', False)
    
    check_type = check_data.get('type', 'unknown')
    interval = check_data.get('interval', 'не указан')
    timeout = check_data.get('timeout', 'не указан')
    
    result = f"### {name}\n\n"
    result += f"**Файл:** `{filename}`\n\n"
    result += f"**Описание:** {description}\n\n"
    result += f"**Тип проверки:** {check_type}\n\n"
    result += f"**Интервал:** {interval} секунд\n\n"
    result += f"**Таймаут:** {timeout} секунд\n\n"
    
    if tags:
        result += f"**Теги:** {', '.join(tags)}\n\n"
    
    if secrets_required:
        result += "⚠️ **Внимание:** Для этой проверки требуется создание секретов в приложении перед использованием.\n\n"
    
    result += "**Использование с cURL:**\n"
    result += "```bash\n"
    result += "curl -X POST \\\n"
    result += "  -H \"Authorization: ВАШ_ТОКЕН\" \\\n"
    result += "  -H \"Content-Type: application/json\" \\\n"
    result += f"  -d @{check_data.get('type', 'multistep')}/{filename} \\\n"
    result += "  https://api.pingera.ru/v1/checks\n"
    result += "```\n\n"
    
    result += "**Использование с Pingera CLI:**\n"
    result += "```bash\n"
    result += f"pngr checks create --from-file {check_data.get('type', 'multistep')}/{filename}\n"
    result += "```\n\n"
    
    result += "**Единоразовый запуск с cURL:**\n"
    result += "```bash\n"
    result += "curl -X POST \\\n"
    result += "  -H \"Authorization: ВАШ_ТОКЕН\" \\\n"
    result += "  -H \"Content-Type: application/json\" \\\n"
    result += f"  -d @{check_data.get('type', 'multistep')}/{filename} \\\n"
    result += "  https://api.pingera.ru/v1/checks/execute\n"
    result += "```\n\n"
    
    result += "**Единоразовый запуск с Pingera CLI:**\n"
    result += "```bash\n"
    result += f"pngr checks run custom --from-file {check_data.get('type', 'multistep')}/{filename}\n"
    result += "```\n\n"
    
    return result

def generate_readme_content(folder_name, checks_data):
    """Генерирует содержимое README файла"""
    folder_display_name = "Многошаговые проверки" if folder_name == "multistep" else "Синтетические проверки"
    
    content = f"# {folder_display_name}\n\n"
    
    if folder_name == "multistep":
        content += "Этот раздел содержит шаблоны многошаговых проверок (multistep checks), которые используют Playwright для выполнения сложных сценариев тестирования API и веб-приложений.\n\n"
        content += "Многошаговые проверки позволяют:\n"
        content += "- Выполнять последовательности HTTP-запросов\n"
        content += "- Тестировать API endpoints\n"
        content += "- Проверять сложные бизнес-процессы\n"
        content += "- Использовать секреты для аутентификации\n\n"
    else:
        content += "Этот раздел содержит шаблоны синтетических проверок (synthetic checks), которые используют Playwright для тестирования веб-интерфейсов и пользовательских сценариев.\n\n"
        content += "Синтетические проверки позволяют:\n"
        content += "- Тестировать пользовательские сценарии\n"
        content += "- Проверять загрузку страниц\n"
        content += "- Делать скриншоты для визуального мониторинга\n"
        content += "- Проверять работу форм и элементов интерфейса\n\n"
    
    content += "## Доступные проверки\n\n"
    
    # Сортируем проверки по имени файла
    sorted_checks = sorted(checks_data.items())
    
    for filename, check_data in sorted_checks:
        content += generate_check_description(check_data, filename)
    
    content += "## Общая информация\n\n"
    content += "### Получение API токена\n\n"
    content += "Для работы с API вам понадобится **API токен**. Вы можете создать его в личном кабинете, в разделе [**\"Настройки\" -> \"API ключи\"**](https://app.pingera.ru/settings/tokens).\n\n"
    
    content += "### Работа с секретами\n\n"
    content += "Некоторые проверки требуют использования [Секретов](https://docs.pingera.ru/checks/secrets). "
    content += "Вы можете создать их заранее через веб-интерфейс, API или CLI:\n\n"
    content += "```bash\n"
    content += "pngr secrets create --name \"SECRET_NAME\" --value \"SECRET_VALUE\"\n"
    content += "```\n\n"
    
    content += "### Регионы выполнения\n\n"
    content += "Большинство проверок настроены для выполнения из следующих регионов:\n"
    content += "- `RU, Moscow` - Москва, Россия\n"
    content += "- `EU, West` - Западная Европа\n"
    content += "- `US, East coast` - Восточное побережье США\n"
    content += "- `IN, Mumbai` - Мумбаи, Индия\n"
    content += "- `QA, Doha` - Доха, Катар\n\n"
    
    content += "Вы можете изменить регионы в конфигурации проверки перед её созданием.\n\n"
    
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
