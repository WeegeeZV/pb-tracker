# runnerlist.py
# Author: Richard Gibson
#
# Lists all runners (users) that have signed up on PB Tracker, sorted by the 
# number of PBs submitted.  This is achieved by calling 
# handler.get_runnerlist( ) that returns a sorted list of dictionaries 
# containing the relevant information. 
#

import handler

class RunnerList( handler.Handler ):
    def get( self ):
        user = self.get_user( )

        runnerlist = self.get_runnerlist( )

        self.render( "runners.html", user=user, runnerlist=runnerlist )
