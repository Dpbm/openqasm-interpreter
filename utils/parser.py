from .error import Error

import os
from pathlib import Path

TARGET_PARSE_RESULT_PATH = os.path.join("..", ".." ,"..", "antlr_results")
SOURCE_DEFAULT_PATH = os.path.join("openqasm", "source", "grammar")

class Parser:
    def __init__(self, source_path:str=SOURCE_DEFAULT_PATH, target_path:str=TARGET_PARSE_RESULT_PATH):
        self.source_path = Path(source_path)
        self.target_path = Path(target_path)


    def parse(self):
        try:
            self.go_to_source()
            print(f"Parsing openqasm to {self.target_path}")
            os.system(f"antlr4 -o {self.target_path} -Dlanguage=Python3 -visitor qasm3Lexer.g4 qasm3Parser.g4")
        except Exception as error:
            Error("parse", error).show()
    
    def go_to_source(self):
        try:
            print(f"Going to {self.source_path}")
            os.chdir(self.source_path)
        except Exception as error:
            Error("go to source", error).show()
