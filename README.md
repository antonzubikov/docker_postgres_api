### **Это REST API контракт для получения англоязычных вопросов для викторин с использованием Flask, Docker, PostgreSQL и ORM SQLAlchemy.**

**Для использования необходимо:**
1. **Установить Docker Engine** на вашу локальную машину (https://docs.docker.com/engine/install/);
2. **Установить все зависимости из файла "requirements.txt"** (`python pip install -r requirements.txt`);
3. **Запустить контейнер с базой данных PostgreSQL на локальной машине** (`docker-compose up -d`);
4. **Запустить файл "main_api.py"** (`python main_api.py`)

**Пример POST запроса**: `localhost:5000/api/questions` (JSON data: "{'questions_num': integer}")