# Classeur

![Logo classeur](classeur_logo.svg "Logo classeur")

Classeur is a tool to merge text files in one then split it to update. Usefull
for writing pandoc/markdown doc

# Install

To install classeur simply clone project then use pip install :

```shell

$ git clone https://github.com/Martoni/Classeur.git
$ cd Classeur
$ python -m pip install .
$ classeur -h
usage: classeur [-h] [-v VERSION] [-m] [-s] [-e] [-c SCISSORS] [-o OUTPUT] markdownfile [markdownfile ...]

merge and split texts files. Version 0.1.0

positional arguments:
  markdownfile          text files to merge, could be markdown or not, whatever.

optional arguments:
  -h, --help            show this help message and exit
  -v VERSION, --version VERSION
                        display version
  -m, --merge           Merge text files in one given by filename argument MERGE
  -s, --split           Split file given in SPLIT argument, then update matching files
  -e, --edit            Edit merged files in $EDITOR and merge them on exit
  -c SCISSORS, --scissors SCISSORS
                        Scissors characters used (default '✂✂✂')
  -o OUTPUT, --output OUTPUT
                        Output filename (default 'document.md')

Simplify pandoc document edition.
```

# Use it

## Merge
Merge all your text files with following command :
```shell
$ classeur -m intro.md chapitre1.md pouet.md annexes.md -o my_merged_doc.md
Merging intro.md
Merging chapitre1.md
Merging pouet.md
Merging annexes.md
Merged 4 files in my_merged_doc.md
```

## Split

Split and update files with :
```shell
$ classeur -s my_merged_doc.md 
Splitting my_merged_doc.md with scissors «✂✂✂»
Found file intro.md
Found file chapitre1.md
Found file pouet.md
Found file intro.md
Found file chapitre1.md
Found file annexes.md
Found file annexes.md
```

## Edit

It's possible to use merged file directly in its favorite editor and merge on
save-exit with edit option :

```shell
$ EDITOR=vim classeur -m intro.md chapitre1.md pouet.md annexes.md
```
# tips

## Vim
Highlight cut line (in neovim .config/nvim/init.vim):
```vim
" Highlight rules for classeur
syntax region classeurCut start=+✂✂✂+ end=+✂✂✂+
highlight classeurCut ctermbg=yellow ctermfg=black
```
