# Classeur

![Logo classeur](classeur_logo.svg "Logo classeur")

Classeur is a useful tool that allows you to merge multiple text files into one and then split it to facilitate updates. It is particularly handy for writing pandoc/markdown documents.

## Merge
To merge all your text files, use the following command:
```shell
$ classeur -m intro.md chapitre1.md pouet.md annexes.md -o my_merged_doc.md
Merging intro.md
Merging chapitre1.md
Merging pouet.md
Merging annexes.md
Merged 4 files into my_merged_doc.md
```

## Split
To split and update files, use the following command:
```shell
$ classeur -s my_merged_doc.md 
Splitting my_merged_doc.md using the scissors "✂✂✂"
Found file intro.md
Found file chapitre1.md
Found file pouet.md
Found file intro.md
Found file chapitre1.md
Found file annexes.md
Found file annexes.md
```

# Vim Tips
If you use neovim, you can use the following configuration in your .config/nvim/init.vim file to highlight cut lines:
```vim
" Highlight rules for classeur
syntax region classeurCut start=+✂✂✂+ end=+✂✂✂+
highlight classeurCut ctermbg=yellow ctermfg=black
```
