from colorama import Fore
from colorama.ansi import AnsiFore
from datetime import datetime
from typing import TextIO
import os, sys

class Logger():
    def __init__(
                self, 
                debug: bool = False, 
                default_prefix: str = None, 
                color_text: bool = False,
                indent_level: int = 0,
                centered: bool = False,
                stream: TextIO = sys.stdout,
                log_file_path: TextIO = None
            ) -> None:
        self.debug_mode = debug
        self.default_prefix = default_prefix
        self.color_text = color_text
        self.indent_level = indent_level
        self.centered = centered
        self.stream = stream
        self.log_file_path = log_file_path
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
        if self.debug_mode:
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
        if self.log_file_path is not None:
            toRemove = []
            for x in AnsiFore.__dict__:
                toRemove.append(AnsiFore.__dict__[x])

            for x in toRemove:
                s = s.replace(f"[{x}m", "")

            try:
                self.log_file_path.write(f"{s}\n")
                self.log_file_path.flush()
            except UnicodeEncodeError as e:
                self.log_file_path.write(f"{s[:e.start] + ' ' + s[e.end:]}\n")
                self.log_file_path.flush()

    def prefix(self, data: str, color: Fore, title: str = None) -> str:
        s = Logger._prefix(
                data=data,
                color=color,
                title=title,
                default_prefix=self.default_prefix,
                color_text=self.color_text,
                centered=self.centered,
                indent_level=self.indent_level
            )
        return s

    def _prefix(data: str, color: Fore, title: str = None, default_prefix: str = None, color_text: bool = False, centered: bool = False, indent_level: int = 0) -> str:
        pr1 = ""
        if not centered: 
            for _ in range(indent_level): 
                pr1 = pr1 + " "

        if default_prefix is not None:
            if "<TIME>" in default_prefix:
                default_prefix = default_prefix.replace("<TIME>", f"{datetime.now().strftime(f'{color}%H{Fore.LIGHTBLACK_EX}:{color}%M{Fore.LIGHTBLACK_EX}:{color}%S')}")
            
            if "|" in default_prefix:
                default_prefix = default_prefix.replace("|", f"{Fore.LIGHTBLACK_EX}|{color}")

            pr1 = pr1 + f"{color}{default_prefix}{Fore.LIGHTBLACK_EX} | "

           
        pr2 = f"{Fore.LIGHTBLACK_EX}({color}{data}{Fore.LIGHTBLACK_EX})"

        full_prefix = f"{pr1}{pr2}"

        if title is not None:
            full_prefix = full_prefix + f" {color}{title}"

        if not color_text: 
            full_prefix = full_prefix + f"{Fore.LIGHTBLACK_EX}"
        
        return full_prefix