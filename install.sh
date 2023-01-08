#!/bin/bash
if [ "$(uname -s)" == "Darwin" ]; then
    brew install portaudio 
else
    echo "ERROR: $(uname -s) install not supported" > /dev/stderr
fi
