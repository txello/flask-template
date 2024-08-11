from .flask import FlaskApp
from importlib import import_module
from .libs import _import_middleware
from .settings import Settings

class Web:
    
    def __init__(self, settings=None) -> None:
        self.__settings = Settings(**{
            field: getattr(settings, field, None) for field in
            [field.name for field in Settings.__dataclass_fields__.values()]
        })
        self.name = self.__settings.FLASK_NAME
        self.app = FlaskApp(self.name)
    
    
    def set_config(self):
        self.app.secret_key = self.__settings.FLASK_SECRET_KEY
    
    def set_dirs(self):
        # set static
        self.app.static_folder = self.__settings.FLASK_DIRS.static
        
        # set template
        self.app.template_folder = self.__settings.FLASK_DIRS.templates
        
    def set_globals(self, globals):
        for func in globals:
            module_name, func_name = func.rsplit('.', 1)
            func = getattr(import_module(module_name), func_name)
            func(self.app)
            
    def set_middlewares(self):
        for middleware in self.__settings.MIDDLEWARES:
            self.app.before_request(_import_middleware(middleware))
    
    def include_routers(self):
        __dir__ = ''
        for router, args in self.__settings.APPS.items():
            if router == '__dir__':
                if args:
                    __dir__ = f"{args}."
                continue
            
            
            dir = f"{__dir__}{router}"
            if self.__settings.VARS.app_init:
                dir += f".{self.__settings.VARS.app_init}"
            
            dir = import_module(dir)
            
            self.app.register_blueprint(getattr(dir, self.__settings.VARS.router), middlewares=args)
        return
    
    def start_app(self):
        self.set_globals(self.__settings.FLASK_GLOBALS.outer)
        self.set_dirs()
        self.set_config()
        self.set_middlewares()
        self.include_routers()
        
        return self.app.run(**self.__settings.FLASK_RUN, globals_inner = self.__settings.FLASK_GLOBALS.inner)