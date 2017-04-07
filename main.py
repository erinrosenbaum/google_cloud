# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import time
from datetime import datetime



class MainPage(webapp2.RequestHandler):
    def get(self):
        # ref: https://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
        the_time = time.strftime("%c")
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!\n')
        self.response.write('Erin Rosenbaum\nCS496 Spring 2017\nApril 7, 2017\nAssignment 1 Getting Started\n')
        self.response.write(the_time)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
