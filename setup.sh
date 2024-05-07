#!/usr/bin/bash
cd ..
mv dragon1 $HOME
mkdir .dragon1
cd dragon1
mv * ../.dragon1
cd ..
rm -rf dragon1
echo "process is now completed !!!"
echo "for starting dragon1 type -->>    dragon1"
