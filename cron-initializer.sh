#/bin/sh

PYTHON=/home/cptbirdy/.virtualenvs/genshin/bin/python3
SCRIPT=/home/cptbirdy/proj/personal/genshin/genshin_login.py
LOG=/tmp/.trash/genshin.log

date > $LOG
$PYTHON $SCRIPT 2>&1 >> $LOG

# source /home/cptbirdy/.virtualenvs/genshin/bin/activate
# python /home/cptbirdy/proj/personal/genshin/genshin/genshin_login.py 2>&1 > $LOG
