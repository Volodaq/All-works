import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Строка подключения
DATABASE_URL = 'postgresql://postgres:72737174@localhost:5433/postgres'

# Создание движка и сессии
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


def test_add_subject():
    session = Session()  # Создание новой сессии

    # Задаем конкретные значения для subject_id и subject_title
    subject_id = 20
    subject_title = 'Algebra'

    # Добавление нового предмета с заданными значениями
    result = session.execute(
        text(
            "INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title) RETURNING subject_id, subject_title"),
        {"id": subject_id, "title": subject_title}
    )
    session.commit()

    # Извлечение вставленных данных
    inserted_subject_id, inserted_subject_title = result.fetchone()

    # Проверка, что предмет добавлен с правильными значениями
    assert inserted_subject_id == subject_id
    assert inserted_subject_title == subject_title

    session.close()  # Закрытие сессии


def test_update_subject():
    session = Session()  # Создание новой сессии

    # Обновление названия предмета
    session.execute(text("UPDATE subject SET subject_title = :new_title WHERE subject_title = :old_title"),
                    {"new_title": "Advanced Mathematics", "old_title": "Algebra"})
    session.commit()

    # Проверка, что предмет изменён
    result = session.execute(text("SELECT subject_title FROM subject WHERE subject_title = :title"),
                             {"title": "Advanced Mathematics"})
    updated_subject_title = result.fetchone()
    assert updated_subject_title is not None and updated_subject_title[0] == "Advanced Mathematics"

    session.close()  # Закрытие сессии


def test_delete_subject():
    session = Session()  # Создание новой сессии

    # Удаление предмета
    session.execute(text("DELETE FROM subject WHERE subject_title = :title"), {"title": "Advanced Mathematics"})
    session.commit()

    # Проверка, что предмет удалён
    result = session.execute(text("SELECT * FROM subject WHERE subject_title = :title"),
                             {"title": "Advanced Mathematics"})
    deleted_subject = result.fetchone()
    assert deleted_subject is None

    session.close()  # Закрытие сессии