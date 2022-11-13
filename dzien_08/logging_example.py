import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    filename="xxx.log",
    format="%(asctime)s %(levelname)-8s %(name)-15s %(message)s'"
)

logging.debug("To jest debug")
logging.info("To jest debug")
logging.warning("To jest debug")
logging.error("To jest debug")
logging.critical("To jest debug")

x = 1
y = 0
try:
    x / y
except ZeroDivisionError as e:
    logging.error(e, stack_info=True, exc_info=True)
    logging.error(f"x={x}, y={y}")


import subprocess

subprocess.run(["ls", "-l"])


# https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Warsaw?unitGroup=metric&key=BAEVLKZKT7EZHTJYCRXYSRDCR&contentType=json