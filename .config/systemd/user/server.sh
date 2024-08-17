[Unit]
Description=tf2 server check

[Service]
ExecStart=%h/.bin/server.sh
WorkingDirectory=/home/cie/.bin/
