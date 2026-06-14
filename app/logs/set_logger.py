import logging


logging.basicConfig(
    level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s",
    filename="log.log")

logger = logging.getLogger(__name__)