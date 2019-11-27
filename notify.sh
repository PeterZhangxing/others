#!/usr/bin/env bash

receiver='root@localhost'

notify(){
    mailtopic="$(hostname) changed to $1:vip floating"
    mailbody="$(date +%F:%T):vrrp_ip floated,$(hostname) changed to $1"
    echo $mailbody | mail -s "$mailtopic" $receiver
}

case $1 in
master)
    notify master
    ;;
backup)
    notify backup
    ;;
fault)
    notify fault
    ;;
*)
    echo "Usage:$(basename $0) {master|backup|fault}"
    ;;
esac