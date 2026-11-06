
"""
===============================================================
       VARIOUS USES OF THE PYTHON LOGGING MODULE
===============================================================
Demonstrations:
1. Logging Levels
2. Formatters
3. Handlers (Console and File)
4. Rotating File Handler
5. Logger Hierarchy
6. Exception Logging
7. Filters
8. Lazy Formatting and Extra Fields
9. Dictionary Configuration
===============================================================
"""

import logging
import logging.config
import logging.handlers
import os
import tempfile


# Create a temporary directory for log files
LOG_DIR = tempfile.mkdtemp(prefix="logdemo_")


def section(title):
    print("\n" + "=" * 8 + " " + title + " " + "=" * 8)


# ---------------------------------------------------------------
# 1. THE FIVE LOGGING LEVELS
# ---------------------------------------------------------------

def demo_levels():
    section("1. Logging Levels")

    log = logging.getLogger("levels")
    log.setLevel(logging.DEBUG)

    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))

    log.addHandler(h)
    log.propagate = False

    log.debug("Detailed information for developers")
    log.info("Normal progress message")
    log.warning("Something unexpected happened")
    log.error("An operation failed")
    log.critical("The program may not continue")

    print("\nRaising threshold to WARNING")

    log.setLevel(logging.WARNING)

    log.debug("This message will not appear")
    log.info("This message will not appear")
    log.warning("This warning will appear")


# ---------------------------------------------------------------
# 2. FORMATTERS
# ---------------------------------------------------------------

def demo_formatter():
    section("2. Formatter")

    log = logging.getLogger("format")
    log.setLevel(logging.INFO)

    h = logging.StreamHandler()

    h.setFormatter(logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | "
        "%(funcName)s:%(lineno)d | %(message)s",
        datefmt="%H:%M:%S"
    ))

    log.addHandler(h)
    log.propagate = False

    log.info("Formatted entry with time, name and level")


# ---------------------------------------------------------------
# 3. HANDLERS - CONSOLE AND FILE
# ---------------------------------------------------------------

def demo_handlers():
    section("3. Console and File Handlers")

    path = os.path.join(LOG_DIR, "app.log")

    log = logging.getLogger("handlers")
    log.setLevel(logging.DEBUG)
    log.propagate = False

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter(
        "CONSOLE %(levelname)s - %(message)s"
    ))

    file_h = logging.FileHandler(path)
    file_h.setLevel(logging.WARNING)
    file_h.setFormatter(logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s"
    ))

    log.addHandler(console)
    log.addHandler(file_h)

    log.debug("Debug message")
    log.info("Info message: console only")
    log.warning("Warning message: console and file")
    log.error("Error message: console and file")

    file_h.flush()

    print("\nContents of app.log:")

    with open(path, "r") as f:
        for line in f:
            print("FILE:", line.rstrip())


# ---------------------------------------------------------------
# 4. ROTATING FILE HANDLER
# ---------------------------------------------------------------

def demo_rotation():
    section("4. Rotating File Handler")

    path = os.path.join(LOG_DIR, "rotate.log")

    log = logging.getLogger("rotate")
    log.setLevel(logging.INFO)
    log.propagate = False

    h = logging.handlers.RotatingFileHandler(
        path,
        maxBytes=200,
        backupCount=2
    )

    h.setFormatter(logging.Formatter("%(message)s"))
    log.addHandler(h)

    for i in range(1, 21):
        log.info("Rotating entry number %d", i)

    h.close()
    log.removeHandler(h)

    print("Files created:")

    files = sorted(
        f for f in os.listdir(LOG_DIR)
        if f.startswith("rotate")
    )

    print(files)


# ---------------------------------------------------------------
# 5. LOGGER HIERARCHY
# ---------------------------------------------------------------

def demo_hierarchy():
    section("5. Logger Hierarchy")

    parent = logging.getLogger("shop")
    parent.setLevel(logging.INFO)
    parent.propagate = False

    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter(
        "[%(name)s] %(message)s"
    ))

    parent.addHandler(h)

    logging.getLogger("shop.cart").info(
        "Item added to cart"
    )

    logging.getLogger("shop.pay").info(
        "Payment accepted"
    )

    logging.getLogger("shop.pay").debug(
        "This debug message is hidden"
    )


# ---------------------------------------------------------------
# 6. EXCEPTION LOGGING
# ---------------------------------------------------------------

def demo_exception():
    section("6. Exception Logging")

    log = logging.getLogger("errors")
    log.setLevel(logging.ERROR)
    log.propagate = False

    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter(
        "%(levelname)s %(message)s"
    ))

    log.addHandler(h)

    try:
        result = 10 / 0

    except ZeroDivisionError:
        log.exception("Division failed")


# ---------------------------------------------------------------
# 7. FILTERS
# ---------------------------------------------------------------

class HideSecrets(logging.Filter):

    def filter(self, record):
        return "password" not in record.getMessage().lower()


def demo_filter():
    section("7. Logging Filters")

    log = logging.getLogger("secure")
    log.setLevel(logging.INFO)
    log.propagate = False

    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter(
        "%(levelname)s %(message)s"
    ))

    h.addFilter(HideSecrets())
    log.addHandler(h)

    log.info("User Rahul logged in")
    log.info("Password for Rahul is 1234")
    log.info("User Rahul opened dashboard")


# ---------------------------------------------------------------
# 8. LAZY FORMATTING AND EXTRA FIELDS
# ---------------------------------------------------------------

def demo_lazy_and_extra():
    section("8. Lazy Formatting and Extra Fields")

    log = logging.getLogger("extras")
    log.setLevel(logging.INFO)
    log.propagate = False

    h = logging.StreamHandler()

    h.setFormatter(logging.Formatter(
        "%(levelname)s user=%(user)s %(message)s"
    ))

    log.addHandler(h)

    log.info(
        "Order %d placed, total Rs.%.2f",
        42,
        1999.5,
        extra={"user": "Rahul"}
    )


# ---------------------------------------------------------------
# 9. DICTIONARY CONFIGURATION
# ---------------------------------------------------------------

def demo_dictconfig():
    section("9. Dictionary Configuration")

    cfg = {
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "short": {
                "format": "%(levelname)s:%(name)s:%(message)s"
            }
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "short",
                "level": "INFO"
            }
        },

        "loggers": {
            "configured": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False
            }
        }
    }

    logging.config.dictConfig(cfg)

    logging.getLogger("configured").info(
        "Configured entirely from a dictionary"
    )


# ---------------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------------

if __name__ == "__main__":

    demo_levels()
    demo_formatter()
    demo_handlers()
    demo_rotation()
    demo_hierarchy()
    demo_exception()
    demo_filter()
    demo_lazy_and_extra()
    demo_dictconfig()

    print("\nLog files were written to:", LOG_DIR)
