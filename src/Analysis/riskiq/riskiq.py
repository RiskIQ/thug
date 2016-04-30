#!/usr/bin/env python
#
# riskiq.py
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA  02111-1307  USA

import os
import traceback
import json
import logging
log = logging.getLogger("Thug")

try:
    from riskiq.api import Client
except ImportError:
    log.error("RiskIQ not installed, disabled.")
    return


class RiskIQ(object):
    def __init__(self):
        self.enabled = True
        self.opts = dict()
        try:
            self.client = Client.from_config()
        except Exception:
            log.error(traceback.format_exc())
            log.error('Failed to load RiskIQ config - disabling RiskIQ plugin.')
            log.error('Please pip install riskiq and run `riq-config setup`')
            self.enabled = False

    def save_report(self, response_dict, basedir, sample):
        log_dir = os.path.join(basedir, 'analysis', 'riskiq')
        content = json.dumps(response_dict)
        log.ThugLogging.log_riskiq(log_dir, sample, content)

    def query(self, sample, basedir):
        # sample is dict, md5 if file
        # return True if successful
        pass

    def analyze(self, data, sample, basedir):
        if not self.enabled:
            return

        # Add riq_query to ThugOpts
        if log.ThugOpts.riq_query:
            # Do query
            pass
