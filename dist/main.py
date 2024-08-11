from core.web import Web
import settings

def main():
    app = Web(settings)
    app.start_app()
    
if __name__ == '__main__':
    main()