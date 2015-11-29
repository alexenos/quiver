#!/usr/bin/python

import argparse

def main() :
   # Parse user options and arguments
   args = arguments()
   print args
   return

def arguments() :
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
   parser_cpp.add_argument('-t', '--trick', help='Generate default Trick headings', action='store_true')
   # Python Parser
   parser_python = subparsers.add_parser('python', help='Python template options')

   # Common arguments
   parser.add_argument('name', help="Name of class and/or file")

   # Parse
   return parser.parse_args()

if __name__ == "__main__" :
   main()
