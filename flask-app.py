from app import app, connector


def main():
    app.run()
    connector.cleanup()


if __name__ == '__main__':
    main()