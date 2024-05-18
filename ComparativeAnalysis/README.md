## Скрипт для анализа Json Резюме и заранее отбранных Json Вакансий
По каждой паре Вакансия - Резюме формируется PDF отчет

## Настройки

- Настройки в файлах `settings.py` и `.env` с точкой (переименовать пример `env`)
- Запуск скрипта `start.py` 
- В функци `start.py` указать выбранный файл резюм и вакансий для анализа, а также, указать ключевой навык из резюме, по которому будет анализироваться опыт. Если ключевой навык не указан, AI попытается определить самостоятельно.

## Стек

- openai