#
# test_namespace.py
#
# the pashmak project
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>
#
# This file is part of pashmak.
#
# pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pashmak.  If not, see <https://www.gnu.org/licenses/>.
##################################################

from TestCore import TestCore

class test_namespace(TestCore):
    def run(self):
        self.assert_output(self.run_without_error('''
        namespace MySpace;
            func dosomething;
                print 'hello world\\n';
            endfunc;

            MySpace.dosomething;
            dosomething;
        endnamespace;

        MySpace.dosomething;
        ''') , 'hello world\nhello world\nhello world\n')