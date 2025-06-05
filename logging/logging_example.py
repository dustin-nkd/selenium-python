# logging.py

import logging

# 1. Basic logging configuration
logging.basicConfig(
    level=logging.DEBUG,                            # Ghi cả DEBUG trở lên
    format="%(asctime)s - %(levelname)s - %(message)s",  # Định dạng log
    filename="app.log",                             # Ghi log vào file (tuỳ chọn)
    filemode="w"                                    # Ghi đè file mỗi lần chạy
)

# 2. Log messages at different severity levels
logging.debug("This is a DEBUG message (useful for developers).")
logging.info("This is an INFO message (general information).")
logging.warning("This is a WARNING message (something unexpected).")
logging.error("This is an ERROR message (something failed).")
logging.critical("This is a CRITICAL message (serious error).")

# 3. Logging in a function
def divide(a, b):
    logging.info(f"Trying to divide {a} by {b}")
    try:
        result = a / b
        logging.debug(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero is not allowed!")
        return None

divide(10, 2)
divide(5, 0)
