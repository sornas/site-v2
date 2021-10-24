" A simple default configuration for beginner Vim usage.
"
" If you have any questions about this file, send an email to
" edvth289@student.liu.se, made with <3 by LiTHe kod.

" This is strictly for Vim, not the ancient Vi.
set nocompatible

" Make sure backspace works as expected, already does on most distros
set backspace=indent,eol,start

" Completion menu for command mode
set wildmenu

" Show current sequence of pressed characters, for instance if pressing 'g'
" display it in the command line
set showcmd

" Set different cursors for different modes
let &t_SI = "\<Esc>[6 q" " line cursor for insert mode
let &t_SR = "\<Esc>[4 q" " underscore cursor for replace mode
let &t_EI = "\<Esc>[2 q" " block cursor for normal mode

" Correct indentation and load options for specific filetypes
filetype plugin indent on
set autoindent

" Better search options, highlight all search matches and allow incremental
" search
set hlsearch
set incsearch

" Mouse support (if you're feeling naughty)
set mouse=a

" Allow hiding unsaved buffers, for instance executing ':e test' from an
" unsaved buffer, on quitting vim will ask to save still
set hidden

" Longer command history
set history=10000

" Keep the undo history, lets you close the buffer and still undo.
" s:data_home for compatibility with neovim
let s:data_home = has('nvim') ? stdpath('data') : expand('~/.vim')
if !isdirectory(s:data_home)
    call mkdir(s:data_home, "", 0770)
endif
let s:undo_dir = s:data_home . '/undo'
if !isdirectory(s:undo_dir)
    call mkdir(s:undo_dir, "", 0700)
endif
let &undodir = s:undo_dir
set undofile

" Gives space around the cursor when scrolling.
set scrolloff=1

" Indents your code 'correctly'.
set tabstop=4 softtabstop=0 expandtab shiftwidth=4 smarttab

" Line numbers, can be useful.
set number

" This command can change your color scheme,
" it has tab-completion if you run it from
" command mode. :D
colorscheme default
" to use correct colorschemes (use rgb colors), uncomment the next line
"set termguicolors

" Ctrl-s to save in both normal mode and insert mode.
" According to me it's a real lifesaver.
nnoremap <C-s> :update<CR>
inoremap <C-s> <ESC>:update<CR>i
" Clear search on CTRL-l as well as redraw screen
nnoremap <C-l> :nohlsearch<CR><C-L>

" Syntax highlighting is nice...
syntax on

" These commands are only enabled for python files.
augroup python
    " Clear python augroup (if config is sourced multiple times)
    autocmd!
    " Show color column at row 81; lines 80 characters or less are
    " recommended.
    autocmd FileType python setlocal colorcolumn=81 textwidth=80

    " Ctrl-g lets you write a grep command to search all python files.
    autocmd FileType python nnoremap <buffer> <C-g> <ESC>:silent copen <BAR> silent grep  *.py<LEFT><LEFT><LEFT><LEFT><LEFT>
    " Save and run (and jump to any error) with <F5>, 
    autocmd FileType python nnoremap <buffer> <F5> :w <BAR> make % <BAR> cwindow <BAR> clast <BAR> redr <CR>

    " TIP: To work even more effectively, try running the ':copen' command
    " after pressing <F5> and the program didn't run. It's pretty cool!
    " (':cn' and ':cp' will help you here!)
    "
    " Say that we're using python scripts here.
    autocmd FileType python setlocal makeprg=python3
    " Make Vim understand what a Python-error is
    autocmd FileType python setlocal errorformat=%-C\ \ \ \ %.%#,%A\ \ File\ \"%f\"\\,\ line\ %l%.%#\,%Z%[%^\ ]%\\@=%m
    " Jumps you to the errors, it's pretty speedy.
    " autocmd FileType python compiler pyunit
augroup END

augroup help
    au!
    " Make it easier to navigate help pages by following tags with enter
    " rather than CTRL-]
    au FileType help nnoremap <buffer> <CR> <C-]>
augroup end
