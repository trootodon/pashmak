#
# test_typeof.py
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

class test_typeof(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        program_vars = self.run_without_error('''
            set $mystr $myint $mybool;

            mem 'the string'; copy $mystr;
            mem 17; copy $myint;
            mem True; copy $mybool;

            set $type_str;
            typeof $mystr; copy $type_str;

            set $type_int;
            typeof $myint; copy $type_int;

            set $type_bool;
            typeof $mybool; copy $type_bool;
        ''')['vars']
        self.assert_equals(type(program_vars['mystr']), str)
        self.assert_equals(type(program_vars['myint']), int)
        self.assert_equals(type(program_vars['mybool']), bool)
        self.assert_equals(program_vars['type_str'], str)
        self.assert_equals(program_vars['type_int'], int)
        self.assert_equals(program_vars['type_bool'], bool)

        self.assert_has_error(self.run_script(''' typeof $notfound; '''), 'VariableError')

        self.assert_has_error(self.run_script(''' typeof gfgfhfh; '''))
