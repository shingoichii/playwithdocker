#! /bin/bash

NEWUSERNAME=${NEWUSERNAME:-ksuser}
NEWPASSWORD=${NEWPASSWORD:-screencast}

# echo $NEWUSERNAME $NEWPASSWORD

addgroup admin
useradd -m --group admin -s /bin/bash $NEWUSERNAME
echo ${NEWUSERNAME}:${NEWPASSWORD} | chpasswd

echo ADDING $NEWUSERNAME DONE.

# hack
exec /sbin/my_init
