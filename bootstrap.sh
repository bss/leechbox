#!/bin/bash
apt-get update

mkdir /data/downloads
mkdir /data/torrents

# Install rtorrent+dep
mkdir .rtorrent_sessions
apt-get install -y rtorrent tmux

# Install btsync
apt-get install -y wget


if [ `getconf LONG_BIT` = "64" ]
then
    wget "http://btsync.s3-website-us-east-1.amazonaws.com/btsync_x64.tar.gz"
    tar xvfz "btsync_x64.tar.gz"
else
    wget "http://btsync.s3-website-us-east-1.amazonaws.com/btsync_i386.tar.gz"
    tar xvfz "btsync_i386.tar.gz"
fi
