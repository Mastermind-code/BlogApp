from Website import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'

#
# if __name__ == '__main__':
#     app.run()
