#!/bin/bash

dir="$(dirname $(realpath $0))"

$dir/src/gen.py $dir/data/mid.mid

timidity $dir/data/mid.mid -Ow -o $dir/data/wav.wav 1>/dev/null

ffmpeg -y -loop 1 -framerate 1 -i $dir/img/cassetti.jpg -i $dir/data/wav.wav -c copy -shortest $dir/data/vid.mkv 1>/dev/null



