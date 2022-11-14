from app import app, db


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(port=12000, debug=True)
    # app.run(host='172.20.10.2', port=9000, debug=True)