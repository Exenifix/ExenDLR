# ExenDLR

Exenifix's Docker Logs Reader

## Description

Module for reading docker logs for GitHub actions. Includes CLI and program tools.

## Usage

### CLI
```shell
$ python3 -m exendlr <container-name> <stop-phrase>

# example
$ python3 -m exendlr my-nice-bot "bot is ready!"
```

### Code
```python
from exendlr import Reader

reader = Reader("my-nice-bot", "bot is ready!")
code = reader.start()

if code == 0:
    print("Bot was started successfully!")
elif code == 1:
    print("There was an error running the bot!")
```
