import ast
import argparse

def parse_tuple(string):
    try:
        return ast.literal_eval(string)
    except (ValueError, SyntaxError) as e:
        raise argparse.ArgumentTypeError(f"Invalid tuple format: {e}")