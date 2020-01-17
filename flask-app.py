from app import app, connector

if __name__ == '__main__':
    app.run()
    connector.cleanup()