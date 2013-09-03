
FROM ubuntu:quantal

MAINTAINER Bo Stendal Sørensen "bo@stendal-sorensen.net"

VOLUME ["/data/downloads", "/data/torrents"]

ADD bootstrap.sh /
ADD rtorrent.rc /.rtorrent.rc
ADD start.py /

RUN /bin/bash bootstrap.sh

ENTRYPOINT ["/usr/bin/python3", "start.py"]