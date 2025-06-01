from loguru import logger
from functools import wraps

logger.add(
    "meu_arquivo_de_log.log",
    format="{time} {level} {message}",
    level="INFO",  
)

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f'chamando função {func.__name__} com argumentos {args} e {kwargs}')
        try:
            result = func(*args, **kwargs)
            logger.info(f'função {func.__name__} retornou {result}')
            return result
        except:
            logger.exception(f'função {func.__name__} falhou')
            raise
    return wrapper