#!/usr/bin/env python
# -*- coding: euc-jp -*-


import sys
from omniORB import CORBA
import Example, Example__POA


orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

loc = "corbaloc:iiop:localhost:2810/test"
obj = orb.string_to_object(loc)
eo = obj._narrow(Example__POA.Echo)


message = "Hello from Python"
result  = eo.echoString(message)
print result