#
# test_free.py
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

''' The test '''

from TestCore import TestCore

class test_free(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        self.assert_vars(self.run_without_error('''
            set $somevar $v1;
            set $hoho;
            free $v1 $hoho;
        '''), {'somevar':None})

        self.assert_mem(self.run_without_error(''' mem 'some thing'; free ^; '''), None)

        self.assert_vars(self.run_without_error(''' free $not_found_var; '''), {})

        self.assert_has_error(self.run_script(''' free $somevar gdhfg ^; '''), 'SyntaxError')
