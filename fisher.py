from app.app import create_app

__auth__ = 'fuhz'

app = create_app()




if __name__ == "__main__":
    app.run(debug=True)
