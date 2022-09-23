if __name__ == '__main__':

    HOST = '0.0.0.0'
    PORT = 26666
    DEBUG = False
    # RELOADER = False

    from app import app
    from process import run_processes_linux, run_processes_win

    run_processes_win()

    app.debug = DEBUG
    app.run(HOST, PORT)
    # app.run(HOST, PORT, use_reloader = RELOADER)