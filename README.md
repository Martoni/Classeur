# Classeur

![Logo classeur](classeur_logo.svg "Logo classeur")

Classeur is a tool to merge text files in one then split it to update. Usefull
for writing pandoc/markdown doc
# Vim tips
Highlight cut line (in neovim .config/nvim/init.vim):
```vim
" Highlight rules for classeur
syntax region classeurCut start=+✂✂✂+ end=+✂✂✂+
highlight classeurCut ctermbg=yellow ctermfg=black
```
