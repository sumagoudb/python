#!/bin/bash
curl https://endocode.com/about/ | grep showTeamMember | sed 's/          <a onclick="showTeamMember(/ /g' | sed "s/'/ /g" | sort | sed 's/)">/ /g' | while read line; do IFS=',' read -r -a array <<< "$line"; initial="$(echo ${array[0]} | head -c 1)"; echo -e $initial'\t'${array[0]}'\t'${array[1]}'\t'${array[2]}; done