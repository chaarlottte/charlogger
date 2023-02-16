# charlogger
A logging library for Python.

I've been using this myself for a while, and I thought that I may as well release it.

It's filled with bad code, but now that it is public, I'll probably improve it over time.

![logger example](https://cdn.upload.systems/uploads/26K4Jvvo.png)

## How to use

### Simple example
```python
import charlogger

logger = charlogger.Logger()
logger.info("What a great logging library!")
```

### Advanced example
```python
import charlogger

# All parameters are optional.
logger = charlogger.Logger(
    debug=True, # Whether to enable the output of debug logs
    defaultPrefix="your prefix",
    colorText=False, # Whether to have the info text be colored
    logFile=open("log.txt", "a"), # The file to put logs in
    indentLevel=8, # The indentation of the text when output.
    centered=True # Whether to center text in the console.
)

logger.info("What a great logging library!")
```

### My personal configuration (best)
```python
import charlogger

logger = charlogger.Logger(
    debug=True,
    defaultPrefix="<TIME> WORKER-001",
    colorText=True
)
logger.info("What a great logging library!")
```

## More in-depth documentation

### `defaultPrefix`
When initializing a Logger, you have the option of `defaultPrefix`.

For now, if you add `"<TIME>"` anywhere in that string, it will replace it with the time of the logging.

For instance, the following code will print `18:26:15 | hi! | i > What a great logging library! `
```python
import charlogger

logger = charlogger.Logger(
    debug=True,
    defaultPrefix="<TIME> hi!"
)
logger.info("What a great logging library!")
```

### Logging methods

Possible arguments
```python
import charlogger

logger = charlogger.Logger()
logger.info("What a great logging library!") # i > What a great logging library! 
logger.info(title="DOCUMENTATION", data="What a great logging library!") # i > [DOCUMENTATION] What a great logging library! 
```

All possible methods
```python
import charlogger

logger = charlogger.Logger()
logger.info("What a great logging library!")
logger.warn("What a great logging library!")
logger.error("What a great logging library!")
logger.debug("What a great logging library!")
logger.valid("What a great logging library!")
logger.invalid("What a great logging library!")
logger.plus("What a great logging library!")
logger.paid("What a great logging library!")
```

Special methods
```python
import charlogger

logger = charlogger.Logger()

# I can't imagine this one being all that useful. It's more there for my personal projects that use it,
logger.choice(1, "Option 1") # 1 > Option 1 

# Will wait for user input in the console.
name = logger.ask("What is your name?") # ? > What is your name? > 
print(name)
```