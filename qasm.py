import sys
from antlr4 import InputStream, CommonTokenStream
from antlr4.tree.Trees import Trees

from utils.parser import Parser 

from antlr_results.qasm3Lexer import qasm3Lexer
from antlr_results.qasm3Parser import qasm3Parser
from antlr_results.qasm3ParserListener import qasm3ParserListener

def execute_code(code):
    input_stream = InputStream(code)
    lexer = qasm3Lexer(input_stream)
    
    token_stream = CommonTokenStream(lexer)
    
    parser = qasm3Parser(token_stream)
    parse_tree = parser.program()
    
    listener = qasm3ParserListener()
    listener.enterProgram(parse_tree)


    print(Trees.toStringTree(parse_tree, None, parser))

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        print("Usage: qasm.py <source_code.qasm>")
        sys.exit(1)

    qasm_source_code = sys.argv[1]
    with open(qasm_source_code, "r") as file:
        source_code = file.read()
    
    execute_code(source_code)
