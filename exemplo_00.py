
from loguru import logger


def soma(x, y):
    try:
        soma = x + y
        logger.info(f'Voce fez correto! parabens! {soma}')
        return soma
    except:
        logger.error('Erro ao somar')
    

soma(2,'3')