export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="agnoster"

plugins=(git)
source $ZSH/oh-my-zsh.sh

# You may need to manually set your language environment
 export LANG=en_US.UTF-8

 alias ohmyzsh="mate ~/.oh-my-zsh"

alias p="python3"

alias ga="git add"
alias gc="git commit"
alias gs="git status"
alias gp="git push"

alias newphp="git clone https://github.com/php/php-src"
alias cchrome="/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --disable-web-security --user-data-dir=~/.cchrome/ --ignore-certificate-errors"

prompt_context() {
  emojis=("🐯" "🧀" "🦋" "🐰" "🍁" "🐶")
  RAND_EMOJI_N=$(( $RANDOM % ${#emojis[@]} + 1))
  if [[ "$USER" == "$DEFAULT_USER" && -n "$SSH_CLIENT" ]]; then
    prompt_segment black default "%(!.%{%F{yellow}%}.)${emojis[$RAND_EMOJI_N]} "
  elif [[ "$USER" != "$DEFAULT_USER" || -n "$SSH_CLIENT" ]]; then
    prompt_segment black default "%(!.%{%F{yellow}%}.)${emojis[$RAND_EMOJI_N]} "
  fi
}

code () { VSCODE_CWD="$PWD" open -n -b "com.microsoft.VSCode" --args $* ;}

source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
