from dataclasses import dataclass
from types import NoneType

@dataclass  
class Dirs:
    static:str|None = None
    templates:str|None = None
    
    def __post_init__(self):
        if isinstance(self.static, NoneType): self.static = 'static/'
        if isinstance(self.templates, NoneType): self.templates = 'templates/'


@dataclass  
class Vars:
    router:str|None = None
    app_init:str|None = None
    
    def __post_init__(self):
        if isinstance(self.router, NoneType): self.router = 'router'

@dataclass
class Globals:
    inner:list|None = None
    outer:list|None = None
    
    def __post_init__(self):
        if isinstance(self.inner, NoneType): self.inner = []
        if isinstance(self.outer, NoneType): self.outer = []
    
@dataclass
class Settings:
    FLASK_NAME:str|None = None
    FLASK_RUN:dict|None = None
    FLASK_SECRET_KEY:str|None = None
    FLASK_DIRS:Dirs|None = None
    FLASK_GLOBALS:Globals|None = None
    MIDDLEWARES:list|None = None
    APPS:dict|None = None
    VARS:Vars|None = None
    
    def __post_init__(self):
        if isinstance(self.FLASK_NAME, NoneType): self.FLASK_NAME = __name__
        if isinstance(self.FLASK_RUN, NoneType): self.FLASK_RUN = {}
        
        if not isinstance(self.FLASK_DIRS, NoneType):
            self.FLASK_DIRS = Dirs(**self.FLASK_DIRS)
        else:
            self.FLASK_DIRS = Dirs()
        
        if not isinstance(self.FLASK_GLOBALS, NoneType):
            self.FLASK_GLOBALS = Globals(**self.FLASK_GLOBALS)
        else:
            self.FLASK_GLOBALS = Globals()
        
        if isinstance(self.MIDDLEWARES, NoneType): self.MIDDLEWARES = []
        if isinstance(self.APPS, NoneType): self.APPS = {}
        
        if not isinstance(self.VARS, NoneType):
            self.VARS = Vars(**self.VARS)
        else:
            self.VARS = Vars()