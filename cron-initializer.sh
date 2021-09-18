#/bin/sh

set -euo pipefail

PYTHON="/home/cptbirdy/.virtualenvs/genshin/bin/python3"
SCRIPT="/home/cptbirdy/proj/personal/genshin/genshin_login.py"
LOG_DIR="/tmp/.trash/"
LOG="$LOG_DIR/genshin.log"

mkdir -p $LOG_DIR

date > $LOG
$PYTHON $SCRIPT 2>&1 >> $LOG

# source /home/cptbirdy/.virtualenvs/genshin/bin/activate
# python /home/cptbirdy/proj/personal/genshin/genshin/genshin_login.py 2>&1 > $LOG
