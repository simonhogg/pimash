#!/bin/bash

sudo python ~pi/pimash/tornadoServer.py &
midori -e Fullscreen -e Navigationbar -e Menubar -e Bookmarkbar -a http://brewery.local &
