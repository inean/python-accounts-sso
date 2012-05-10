#!/bin/sh

rm -rf build
mkdir -p build
cd build && cmake ..

echo 
echo "type cd build && make to build this"
echo "type cd build && make install to install this"
echo
