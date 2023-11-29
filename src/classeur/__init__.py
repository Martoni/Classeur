import re
import argparse
import pkg_resources  # part of setuptools
version = pkg_resources.require("classeur")[0].version

SCISSORS = "✂✂✂"
DEFAULT_OUTPUT = "document.md"

def merging(markdownfiles, outputfilename, scissors):
    with open(outputfilename, "w") as fpo:
        for filename in markdownfiles:
            print(f"Merging {filename}")
            with open(filename, "r") as fp:
                fpo.write(f"{scissors} {filename} {scissors}\n")
                for line in fp:
                    fpo.write(line)

    print(f"Merged {len(markdownfiles)} files in {outputfilename}")

def splitting(markdownfile, scissors):
    print(f"Splitting {markdownfile} with scissors «{scissors}»")
    regexp = re.compile(f"^{SCISSORS}(.*){SCISSORS}$")
    openfile = None
    with open(markdownfile) as fps:
        for line in fps:
            if regexp.match(line):
                filename = regexp.search(line).group(1).strip()
                print(f"Found file {filename}")
                if not openfile is None:
                    openfile.close()
                openfile = open(filename, "w")
            else:
                if not openfile is None:
                    openfile.write(line)
                else:
                    raise Exception("Format error")


def main():
    parser = argparse.ArgumentParser(
                    prog='classeur',
                    description=f'merge and split texts files. Version {version}',
                    epilog='Simplify pandoc document edition.') 
    parser.add_argument('markdownfile', metavar='markdownfile',
            type=str, nargs='+',
            help="text files to merge, could be markdown or not, whatever. ")
    parser.add_argument('-v', '--version', help="display version", )
    parser.add_argument('-m', '--merge', action='store_true',
            help="Merge text files in one given by filename argument MERGE")
    parser.add_argument('-s', '--split', action='store_true',
            help="Split file given in SPLIT argument, then update matching files")
    parser.add_argument("-c", "--scissors", default=SCISSORS,
            help=f"Scissors characters used (default '{SCISSORS}')")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT, 
            help=f"Output filename (default '{DEFAULT_OUTPUT}')")
  
    args = parser.parse_args()

    markdownfiles = args.markdownfile
    merge = args.merge
    split = args.split
    scissors = args.scissors
    outputfilename = args.output

    if merge and split:
        return Exception("can't both merge and split at same time, choose one")

    if merge:
        merging(markdownfiles, outputfilename,  scissors)
    elif split:
        splitting(markdownfiles[0], scissors)
    else:
        print("Do you want to merge (-m) or split (-s) ?")
