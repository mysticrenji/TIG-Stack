#!/bin/bash

# Usage: ./latencytest.sh $argument

if [ $# -eq 0 ]
   then
    echo ""
    echo "    Latency Test       latencytest.sh"
    echo "------------------------------------------"
    echo "none     = no latency change"
    echo "low    = 100 ms"
    echo "medium   = 500 ms"
    echo "high   = 1000 ms"
    echo "show   = Current latency profile"
    echo ""
   exit
 fi

if [ $1 = "none" ]
   then
     echo "netem latency profile off"
     tc qdisc del dev wlan0 root netem
   exit
 fi

if [ $1 = "show" ]
   then
     echo "show netem latency profile"
     tc qdisc show dev wlan0
   exit
 fi

if [ $1 = "low" ]
   then
     echo "Adding latency 100ms"
     tc qdisc add dev wlan0 root netem delay 100ms
   exit
 fi

if [ $1 = "medium" ]
   then
      echo "Adding latency 500ms"
     tc qdisc add dev wlan0 root netem delay 500ms
   exit
 fi

if [ $1 = "high" ]
   then
      echo "Adding latency 1000ms"
     tc qdisc add dev wlan0 root netem delay 1000ms
   exit
 fi

#### EOF #####
