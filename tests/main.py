import charlogger

logger = charlogger.Logger(
    debug=True,
    default_prefix="<TIME> | WORKER-001",
    color_text=False,
    # log_file_path=open("log.txt", "a")
    # indent_level=8,
    # centered=True
)

logger.info("Solved captcha - 8690281096.68002176")
logger.warn("Ratelimited! Retrying in 3s...")
logger.error("Error! Could not get property 'thing'.")
logger.debug("Took 3.521s to fetch items.")
logger.valid("Valid account - test@gmail.com:jgilo3h3h06824l;")
logger.invalid("Invalid account - test@gmail.com:jgilo3h3h06824l;")
logger.plus("I don't really remember what this was for, to be honest.")
logger.paid("Bought on test@gmail.com.")
logger.choice(1, "Option 1")
print()

logger.info(title="SOLVED", data="Solved captcha - 8690281096.68002176")
logger.warn(title="WARNING", data="Ratelimited! Retrying in 3s...")
logger.error(title="ERROR", data="Error! Could not get property 'thing'.")
logger.debug(title="DEBUG", data="Took 3.521s to fetch items.")
logger.valid(title="VALID", data="Valid account - test@gmail.com:jgilo3h3h06824l;")
logger.invalid(title="INVALID", data="Invalid account - test@gmail.com:jgilo3h3h06824l;")
logger.plus(title="PLUS", data="I don't really remember what this was for, to be honest.")
logger.paid(title="PAID", data="Bought on test@gmail.com.")
logger.choice(1, title="1", data="Option 1")