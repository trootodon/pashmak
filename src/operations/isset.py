# isset.py
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

def run(self , op):
    args = op['args_str'].split(' ')
    for arg in args:
        if len(arg) > 0:
            if arg[0] == '$':
                varname = arg[1:]
                try:
                    tmp = self.variables[varname]
                except:
                    self.mem = False
                    return
            else:
                self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)
            
    self.mem = True