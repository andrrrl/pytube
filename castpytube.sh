#!/bin/bash

youtube-dl -o - "$1" | castnow --quiet "$2"
