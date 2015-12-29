#!/usr/bin/python

import argparse
import tabula

def main() :
   # Parse user options and arguments
   args = user_input()
   # Define the blank slate
   slate = tabula.create(args)
   # Write! It shall no longer be blank
   slate.write()
   return

def user_input() :
   # Setup main parser
   parser = argparse.ArgumentParser(
           description ="Autogenerates simple, blank templates for a handful of languages with limited options",
           epilog="Report bugs to dax.garner@gmail.com",
           version="0.1",
           argument_default=True
           )

   # Setup language parsers
   subparsers = parser.add_subparsers(dest='language', metavar='language', help='Language specific options')
   # C++ Parser
   parser_cpp = subparsers.add_parser('cpp', help='C++ template options')
   parser_cpp.add_argument('-t', '--trick', help='Generate default Trick headings', action='store_true', default=False)
   # Python Parser
   parser_python = subparsers.add_parser('python', help='Python template options')

   # Common arguments
   parser.add_argument('name', help="Name of class and/or file")
   parser.add_argument('-c', '--class', help="Creates a file containing a class definition", action='store_true', default=True)
   parser.add_argument('-m', '--main', help="Creates a file designated as the top-level main", action='store_true', default=False)

   # Parse
   return parser.parse_args()

if __name__ == "__main__" :
   main()
