# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
ZSH_THEME="robbyrussell_custom"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git svn catimg )

source $ZSH/oh-my-zsh.sh

# User configuration

# Exports and zsh options
# opt/local/bin&sbin for macports
export PATH="/usr/local/sbin:/usr/local/bin:/usr/bin:/opt/cuda/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:/opt/mpich/bin"
export GL_ENABLE_DEBUG_ATTACH YES
export LD_LIBRARY_PATH="/opt/mpich2/lib:/home/tims/code/testbed/common"
export PYTHONSTARTUP=~/.pythonrc
setopt nobeep

# Special key bindings
bindkey '\e' vi-cmd-mode
#bindkey "\eOA" up-line-or-local-history
#bindkey "\eOB" down-line-or-local-history

up-line-or-local-history() {
    zle set-local-history 1
    zle up-line-or-history
    zle set-local-history 0
}
zle -N up-line-or-local-history
down-line-or-local-history() {
    zle set-local-history 1
    zle down-line-or-history
    zle set-local-history 0
}
zle -N down-line-or-local-history

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.

# Git aliases (no need for these with git plugin for zsh)
# This diff shortcut doesnt work if youre not in root of repo
#git_diff_shortcut() {
#git status --porcelain | sed -n "${1} s/^...//p" | xargs  git diff
#}
#alias gd=git_diff_shortcut
#alias gs="git status"
#alias ga="git add"
#alias gc="git commit"
#alias gb="git branch"
#alias gco="git checkout"
#alias gp="git push"
#alias gpo="git push origin"

# Zsh
alias zshconfig="vim ~/.zshrc"
alias ohmyzsh="vim ~/.oh-my-zsh"
alias rezsh="source ~/.zshrc"

# Configs
alias termconfig="vim ~/.config/terminator/config"
alias xmonadconfig="vim ~/.xmonad/xmonad.hs"
alias gtk3config="sudo vim /usr/share/gtk-3.0/settings.ini"
alias gtk2config="sudo vim /usr/share/gtk-2.0/gtkrc"

# Others
#alias ls="ls -G"
alias ll="ls -l"
alias la="ls -a"
#alias paraview="/Users/tims/Programs/paraview/build/bin/paraview.app/Contents/MacOS/paraview"
#alias openheader="open -a 'Sublime Text 3' -h"
#alias subl="open -a 'Sublime Text 3'"
#alias texcount="perl /Users/tims/Programs/texcount/texcount.pl"

tga2avi() { mencoder -nosound 'mf://*.tga' -mf w=800:h=800:fps="$@":type=tga -ovc x264 -x264encopts bitrate=3000 -o output_compressed_x264.avi } 
#example alias with argument
img2avi() { mencoder -nosound "mf://*.${1}" -mf w=800:h=800:fps="$2":type=$1 -ovc x264 -x264encopts bitrate=3000 -o output_compressed_x264.avi } 
