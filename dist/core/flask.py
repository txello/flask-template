from flask import Flask
from importlib import import_module

class FlaskApp(Flask):
    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        globals_inner = options.pop('globals_inner', [])
        with self.app_context():
            self.set_globals(globals_inner)
        
        super().run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)

    def set_globals(self, globals):
        for func in globals:
            module_name, func_name = func.rsplit('.', 1)
            func = getattr(import_module(module_name), func_name)
            func(self)