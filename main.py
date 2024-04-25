from db.engine import db, app


try:
    with app.app_context():
        db.create_all()
except Exception as e:
    print(f"Ошибка при создании таблиц: {e}")

app.run(debug=True)
