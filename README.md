# task_qa_keysystems_playwright
Тестовое задание на позицию инженера по организации автоматизированного тестирования

## Задача 

Обеспечить прикладное тестирование комплекса.

Сценарий тестирования:
- _минимум_
  
  - Прогрузка стартовой страница (убедится в наличии полей ввода)
  - Ввод неверного логина и пароля
  - Ввод верного логина и пароля
- _средне_
  
  - Проверка прогрузки навигатора и десктопа
  - Открытия режима "Ежедневный" из навигатора
- _максимум_

  - Ввод любого документа (на выбор)
  - Проверка, что документ появился в списке
- _ультра_
  
  Анализ Ошибок: 
    1. В качестве ошибки на рабочем столе приходит информационная ошибка о неверной настроенной базе
    2. При выборе Меню-Сервис-Журнал ошибок выходит серьезная ошибка

 В отчете указать действие и успешность (да/нет)


Язык - любой

Веб драйвер - любой

Допустимость использование микроядер по типу Chromium - да

## Необходимый результат
  Приложение в которое вводится адрес, логин, пароль. 
  
  По результатам приложения - структурированный отчет о проведенном тестировании.

## Описание проекта
Проект реализован с помощью паттерна проектирования Page Object. В качестве инструмента тестирования выбран Playwright. 

## Системные требования для Playwright
- Python 3.8 or higher.
- Windows 10+, Windows Server 2016+ or Windows Subsystem for Linux (WSL).
- MacOS 12 Monterey or MacOS 13 Ventura.
- Debian 11, Debian 12, Ubuntu 20.04 or Ubuntu 22.04.


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Zima2022/task_qa_keysystems_playwright.git
```
```
cd task_qa_keysystems_playwright
```

Создать и активировать виртуальное окружение:

- для Linux
```
python3.10 -m venv venv
source venv/bin/activate
```
- для Windows
```
py -3.10 -m venv venv 
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Установить поддерживаемые Playwright браузеры:
```
playwright install
```

В корне проекта создать файл `.env`. Прописать в нём переменные окружения URL, LOGIN и PASSWORD. Например:
```
URL=https://dsr01.keysystems.ru:5444/tracker_test/
LOGIN=some_login
PASSWORD=some_password
```

Запускаем тесты с помощью команды:
```
pytest -v
```
Тесты по умолчанию запускаются в браузере Chrome в headless режиме (во время тестирования нет видимого графического 
пользовательского интерфейса браузера).

Отчет о тестировании так же можно сформировать в Allure. В связи с тем, что не успел проверить установку Allure
на Linux, соответствующих инструкций пока нет. Добавлю, когда проверю.

### Возможные проблемы и способы их устранения
Если возникнет проблема с библиотекой `python-dotenv`, то удалить файл `conftest.py`, а в файле `test_data.py` 
прописать URL, LOGIN, PASSWORD:
```
URL = 'Прописать url'
LOGIN = 'Прописать логин'
PASSWORD = 'Прописать пароль'
```
### Обратная связь, если есть вопросы
telegram: @iamutin
