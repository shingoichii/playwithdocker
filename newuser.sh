#! /bin/bash

NEWUSERNAME=${NEWUSERNAME:-ksuser}
NEWPASSWORD=${NEWPASSWORD:-screencast}

# echo $NEWUSERNAME $NEWPASSWORD
useradd -m --group admin -s /bin/bash $NEWUSERNAME
"${NEWUSERNAME}:${NEWPASSWORD} | chpasswd"
