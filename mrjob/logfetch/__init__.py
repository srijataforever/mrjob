# Copyright 2009-2011 Yelp and Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import with_statement

import glob
import os
import re


# use to detect globs and break into the part before and after the glob
GLOB_RE = re.compile(r'^(.*?)([\[\*\?].*)$')


class LogFetchException(Exception):
    pass


class LogFetcher(object):

    def __init__(self, local_temp_dir='/tmp'):
        super(LogFetcher, self).__init__()
        self.local_temp_dir = local_temp_dir

    def task_attempts_log_uri_re(self):
        raise NotImplementedError

    def step_log_uri_re(self):
        raise NotImplementedError

    def job_log_uri_re(self):
        raise NotImplementedError

    def ls(self, path):
        """Recursively list all files in the given path.

        We don't return directories for compatibility with S3 (which
        has no concept of them)

        Corresponds roughly to: ``hadoop fs -lsr path_glob``
        """
        for path in glob.glob(path_glob):
            if os.path.isdir(path):
                for dirname, _, filenames in os.walk(path):
                    for filename in filenames:
                        yield os.path.join(dirname, filename)
            else:
                yield path

    def get(self, path):
        """Download the file at ``path`` and return its local path
        """
        return path
