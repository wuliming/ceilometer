#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright © 2012 eNovance <licensing@enovance.com>
#
# Author: Julien Danjou <julien@danjou.info>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import subprocess
import unittest
import tempfile
import os


class BinDbsyncTestCase(unittest.TestCase):
    def setUp(self):
        self.tempfile = tempfile.mktemp()
        with open(self.tempfile, 'w') as tmp:
            tmp.write("[DEFAULT]\n")
            tmp.write("database_connection=log://localhost\n")

    def test_dbsync_run(self):
        subp = subprocess.Popen(["../bin/ceilometer-dbsync",
                                 "--config-file=%s" % self.tempfile])
        self.assertEqual(subp.wait(), 0)

    def tearDown(self):
        os.unlink(self.tempfile)
