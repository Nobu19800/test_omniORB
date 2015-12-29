#!/usr/bin/env python

import sys, os
from omniORB import CORBA, PortableServer

import Example, Example__POA


class Echo_i (Example__POA.Echo):
    def echoString(self, mesg):
        print "echoString() called with message:", mesg
        return mesg


sys.argv.extend(["-ORBendPoint","giop:tcp::2810"])

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)



ei = Echo_i()
eo = ei._this()



poa = orb.resolve_initial_references("omniINSPOA")
poa._get_the_POAManager().activate()
id = "test"
poa.activate_object_with_id(id, ei)

orb.run()
