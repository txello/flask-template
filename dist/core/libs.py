from importlib import import_module

def _import_middleware(middleware_path):
        module_name, class_name = middleware_path.rsplit('.', 1)
        module = import_module(module_name)
        middleware_class = getattr(module, class_name)
        return middleware_class()