from colorama import Fore
from colorama.ansi import AnsiFore
from datetime import datetime
from typing import TextIO
import os, sys

class Logger():
    def __init__(
                self, 
                debug: bool = False, 
                defaultPrefix: str = None, 
                colorText: bool = False,
                indentLevel: int = 0,
                centered: bool = False,
                stream: TextIO = sys.stdout,
                logFile: TextIO = None
            ) -> None:
        self.debugMode = debug
        self.defaultPrefix = defaultPrefix
        self.colorText = colorText
        self.indentLevel = indentLevel
        self.centered = centered
        self.stream = stream
        self.logFile = logFile
        pass

    def info(self, data: str, title: str = None) -> None:
        prefix = self.prefix("i", Fore.LIGHTBLUE_EX, title)
        self.output(f"{prefix} {data} {Fore.RESET}")

    def warn(self, data: str, title: str = None) -> None:
        prefix = self.prefix("!", Fore.YELLOW, title)
        self.output(f"{prefix} {data} {Fore.RESET}")

    def error(self, data: str, title: str = None) -> None:
        prefix = self.prefix("!", Fore.RED, title)
        self.output(f"{prefix} {data} {Fore.RESET}")

    def debug(self, data: str, title: str = None) -> None:
        if self.debugMode:
            prefix = self.prefix("~", Fore.LIGHTMAGENTA_EX, title)
            self.output(f"{prefix} {data} {Fore.RESET}")

    def valid(self, data: str, title: str = None) -> None:
        prefix = self.prefix("✓", Fore.LIGHTGREEN_EX, title)
        self.output(f"{prefix} {data} {Fore.RESET}")

    def invalid(self, data: str, title: str = None) -> None:
        prefix = self.prefix("-", Fore.LIGHTRED_EX, title)
        self.output(f"{prefix} {data} {Fore.RESET}")

    def plus(self, data: str, title: str = None) -> None:
        prefix = self.prefix("+", Fore.LIGHTGREEN_EX, title)
        self.output(f"{prefix} {data} {Fore.RESET}")

    def paid(self, data: str, title: str = None) -> None:
        prefix = self.prefix("$", Fore.LIGHTCYAN_EX, title)
        self.output(f"{prefix} {data} {Fore.RESET}")

    def ask(self, data: str, title: str = None) -> str:
        prefix = self.prefix("?", Fore.LIGHTBLUE_EX, title)
        return input(f"{prefix} {data} {Fore.RESET}> ")

    def choice(self, i: int, data: str, title: str = None) -> None:
        prefix = self.prefix(i, Fore.LIGHTBLUE_EX, title)
        self.output(f"{prefix} {data} {Fore.RESET}")

    def output(self, s: str) -> None:
        if self.centered:
            self.stream.write(f"{s.center(os.get_terminal_size().columns)}\n")
            self.stream.flush()
        else:
            self.stream.write(f"{s}\n")
            self.stream.flush()

        # Please never look at this code
        if self.logFile is not None:
            toRemove = []
            for x in AnsiFore.__dict__:
                toRemove.append(AnsiFore.__dict__[x])

            for x in toRemove:
                s = s.replace(f"[{x}m", "")

            try:
                self.logFile.write(f"{s}\n")
                self.logFile.flush()
            except UnicodeEncodeError as e:
                self.logFile.write(f"{s[:e.start] + ' ' + s[e.end:]}\n")
                self.logFile.flush()

    def prefix(self, data: str, color: Fore, title: str = None) -> str:
        s = Logger._prefix(
                data=data,
                color=color,
                title=title,
                defaultPrefix=self.defaultPrefix,
                colorText=self.colorText,
                centered=self.centered,
                indentLevel=self.indentLevel
            )
        return s

    def _prefix(data: str, color: Fore, title: str = None, defaultPrefix: str = None, colorText: bool = False, centered: bool = False, indentLevel: int = 0) -> str:
        pr1 = ""
        if not centered: 
            for _ in range(indentLevel): 
                pr1 = pr1 + " "

        if defaultPrefix is not None:
            if "<TIME>" in defaultPrefix:
                defaultPrefix = defaultPrefix.replace("<TIME>", f"{datetime.now().strftime(f'{color}%H{Fore.WHITE}:{color}%M{Fore.WHITE}:{color}%S')}{Fore.WHITE} |{color}")
                
            pr1 = pr1 + f"{color}{defaultPrefix}{Fore.RESET} | "

           
        pr2 = f"{color}{data} >"

        fullPrefix = f"{pr1}{pr2}"

        if title is not None:
            fullPrefix = fullPrefix + f" {Fore.WHITE}[{color}{title}{Fore.WHITE}]{color}"

        if not colorText: 
            fullPrefix = fullPrefix + f"{Fore.RESET}"
        
        return fullPrefix