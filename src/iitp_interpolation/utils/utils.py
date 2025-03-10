import argparse
import ast


def parse_tuple(string: str):
    try:
        return ast.literal_eval(string)
    except (ValueError, SyntaxError) as e:
        raise argparse.ArgumentTypeError(f"Invalid tuple format: {e}") from e