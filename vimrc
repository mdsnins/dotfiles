set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'scrooloose/nerdtree'
Plugin 'scrooloose/syntastic'
cal vundle#end()

filetype plugin indent on

map <Leader>nt <ESC>:NERDTree<CR>

set t_Co=256
set background=dark
set mouse=a
syntax on

set autoindent
set cindent
set smartindent
set tabstop=4
set expandtab
set shiftwidth=4

filetype indent on

set nu

set laststatus=2
set statusline=\ %c%l:%v\ [%P]%=%a\ %h%m%r\ %F\
