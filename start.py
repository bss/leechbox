#!/usr/bin/env python
import argparse
import json
import os

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(help="BT Sync secret for the data dir.",
                        dest='BT_SECRET_DATA')

    parser.add_argument(help="BT Sync secret for the torrents dir.",
                        dest='BT_SECRET_TORRENTS')

    args = parser.parse_args()

    config = {  "device_name": "Leech Box",
                "listening_port" : 31337,
                "check_for_updates" : True,
                "use_upnp" : True,
                "download_limit" : 0,
                "upload_limit" : 0,
                "shared_folders" : [
                    {
                      "secret" : args.BT_SECRET_DATA,
                      "dir" : "/data/downloads",
                      "use_relay_server" : False,
                      "use_tracker" : True,
                      "use_dht" : False,
                      "search_lan" : False,
                      # Enable sync trash to store files deleted on remote devices
                      "use_sync_trash" : False,
                      "known_hosts" : []
                    },
                    {
                      "secret" : args.BT_SECRET_TORRENTS,
                      "dir" : "/data/torrents",
                      "use_relay_server" : False,
                      "use_tracker" : True,
                      "use_dht" : False,
                      "search_lan" : False,
                      # Enable sync trash to store files deleted on remote devices
                      "use_sync_trash" : False,
                      "known_hosts" : []
                    },
                ],
             }
    with open('btsync.conf', 'w') as f:
        json.dump(config, f, ensure_ascii=False)

    os.system("./btsync --config btsync.conf")
    # os.system("rtorrent")
    os.system("/bin/bash")
