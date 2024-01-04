# Classeur

![Logo classeur](classeur_logo.svg "Logo classeur")

Classeur is a tool to merge text files in one then split it to update. Usefull
for writing pandoc/markdown doc

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
 classeur -s my_merged_doc.md 
Splitting my_merged_doc.md with scissors «✂✂✂»
Found file intro.md
Found file chapitre1.md
Found file pouet.md
Found file intro.md
Found file chapitre1.md
Found file annexes.md
Found file annexes.md
```


# Vim tips
Highlight cut line (in neovim .config/nvim/init.vim):
```vim
" Highlight rules for classeur
syntax region classeurCut start=+✂✂✂+ end=+✂✂✂+
highlight classeurCut ctermbg=yellow ctermfg=black
```
