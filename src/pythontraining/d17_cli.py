"""
Demo of the argparse module
"""
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("number", help="print the given number * 2")
args = parser.parse_args()

doubled = args.number * 2

print(doubled)

