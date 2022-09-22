import logging

logger = logging

logger.basicConfig(level=logging.WARN,
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                   datefmt='%I:%M:%S %p',
                   handlers=[logging.FileHandler('capa_datos.log'),  # Manda la información al archivo
                             logging.StreamHandler()])