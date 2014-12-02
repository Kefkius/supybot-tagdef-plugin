###
# Copyright (c) 2014, Tyler Willis
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import requests
import json

class Tagdef(callbacks.Plugin):
    """Use the command 'tagdef <hashtag>' to
    retrieve its definition"""

    def __init__(self, irc):
        self.__parent = super(Tagdef, self)
        self.__parent.__init__(irc)
        self.url = 'http://api.tagdef.com/'

    def tagdef(self, irc, msg, args, tagname):
        """<hashtag>

        Retrieves the definition of <hashtag>"""
        req_url = ''.join([self.url, 'one.', tagname, '.json'])
        resp = requests.get(req_url).json()['defs']['def']
        try:
            retstr = '#{0}: {1}'.format(resp['hashtag'], resp['text'])
        except KeyError:
            retstr = 'Error: Could not retrieve hashtag definition'
        irc.reply(retstr)
    tagdef = wrap(tagdef, ['somethingWithoutSpaces'])

Class = Tagdef


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
