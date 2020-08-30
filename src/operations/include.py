# include.py
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
# along with cati.  If not, see <https://www.gnu.org/licenses/>.
##################################################

from syntax import parser

def run(self , op):
    args = op['args_str'].strip().split(' ')

    if len(args) <= 0:
        self.raise_error('SyntaxError' , 'include command gets a parameter' , op)

    arg = args[0]

    if arg != '':
        if arg == '^':
            path = self.get_mem()
        else:
            if arg[0] == '%':
                try:
                    path = self.variables[arg[1:]]
                except:
                    self.raise_error('VariableError' , 'undefined variable "' + arg + '"' , op)
            else:
                self.raise_error('SyntaxError' , 'unexpected "' + arg[0] + '"' , op)
            
        try:
            content = open(path , 'r').read()
            operations = parser.parse(content)
            for operation in operations:
                self.run(operation)
        except Exception as ex:
            self.raise_error('FileError' , str(ex) , op)
    else:
        self.raise_error('SyntaxError' , 'include command gets a parameter' , op)