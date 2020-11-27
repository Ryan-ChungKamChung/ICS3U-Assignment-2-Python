#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# Program finds the surface area of a sphere


import math


def main():
    # This function finds the surface area of a sphere

    # Input
    print("This program finds the surface area of a sphere!")
    radius = int(input("Please enter a radius (mm): "))

    # Process
    surface_area = 4 * math.pi * radius**2

    # Output
    print("The surface area is: {}mm".format(surface_area))


if __name__ == "__main__":
    main()
