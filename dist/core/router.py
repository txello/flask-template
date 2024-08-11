from flask import Blueprint
from .libs import _import_middleware

class Router(Blueprint):
    def register(self, app, options):
        super().register(app, options)
        middlewares = options.get('middlewares', [])
        for middleware_path in middlewares:
            app.before_request_funcs.setdefault(self.name, []).append(_import_middleware(middleware_path))