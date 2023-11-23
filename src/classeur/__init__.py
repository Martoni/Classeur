import argparse


def main():
    parser = argparse.ArgumentParser(
                    prog='classeur',
                    description='merge and split texts files',
                    epilog='Simplify pandoc edition') 
    parser.add_argument('filename') # positional argument
    args = parser.parse_args()

    print("classeur command")
