#!/usr/bin/python
"""Scale line/arc plots and circular/rectangular apertures in Gerber files. This is useful for fabricating multilayer PDMS devices because the top layer will shrink prior to alignment, so wafer features need to be scaled.

Example usage to scale by 1.5% :
python gerber_scaling.py -i "input/file/location.gbr" -s 1.015

Note:
This will only scale circular and rectangular apertures as well as point coordinates in an X#Y#D# format.
"""
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str)
parser.add_argument("-s", "--scale", type=float)

args = parser.parse_args()
input_file = args.input
scale = args.scale

output_file = input_file[:-4] + '_scaled_' + str(scale) + '.gbr'

# Regular expression constructs
reX = re.compile('X')  # Finds'X'
reY = re.compile('Y')  # Finds 'Y'
reI = re.compile('I')  # Finds 'I'
reJ = re.compile('J')  # Finds 'J'
reD = re.compile('D')  # Finds 'D'
rec = re.compile(',')  # Finds ','
res = re.compile('\*')  # Finds '*'
reAC = re.compile('^%ADD[0-9]+C')  # Finds circle apertures
reAR = re.compile('^%ADD[0-9]+R')  # Finds rectangle apertures
reXY = re.compile('^X-?[0-9]+Y-?[0-9]+D')  # Finds linear plots
reXYIJ = re.compile('^X-?[0-9]+Y-?[0-9]+I-?[0-9]+J-?[0-9]+D')  # Finds arc plots

def scaleLinear(line,scale):
    """Scale linear plots.

    Finds the first and second digit of the point, scales them, and the outputs the original line with scaled digits. Assumes that points have the following format:

    X114000000Y-64275000D02*
    X#Y#Di*
    """
    y = reY.search(line)
    d = reD.search(line)
    d1 = int(line[1:y.start()]) * scale
    d2 = int(line[y.start()+1:d.start()]) * scale
    return 'X' + str(round(d1)) + 'Y' + str(round(d2)) + line[d.start():]

def scaleArc(line, scale):
    """Scale arc plots.

    Finds the first to fourth digits of the arc, scales them, and the outputs the original line with scaled digits. Assumes that points have the following format:

    X14000000Y-64275000I-50000000J0D01*
    X#Y#I#J#Di*
    """
    y = reY.search(line)
    i = reI.search(line)
    j = reJ.search(line)
    d = reD.search(line)
    d1 = float(line[1:y.start()]) * scale  # Scale first digit
    d2 = float(line[y.start()+1:i.start()]) * scale  # Scale second digit
    d3 = float(line[i.start()+1:j.start()]) * scale
    d4 = float(line[j.start()+1:d.start()]) * scale
    return 'X' + str(round(d1)) + 'Y' + str(round(d2)) + 'I' + str(round(d3)) + 'J' + str(round(d4)) + line[d.start():]


def scaleCircle(line, scale):
    """Scale predefined circular apertures.

    Finds the first and second digit of the aperture, scales them, and the outputs the original line with scaled digits. Assumes that circles have the following format:

    %ADD10C,1.000000*%
    %ADDiC,N*%
    """
    comma = rec.search(line)
    s = res.search(line)
    l = len(line[comma.start()+1:s.start()])
    d1 = float(line[comma.start()+1:s.start()])*scale  # Scale first digit
    dl1 = l - len(str(int(d1))) -1  # Adjust format precision by number of leading digits + ','
    return line[0:comma.start()+1] + format(d1,f'.{dl1}f') + line[s.start():]

def scaleRectangle(line,scale):
    """Scale predefined rectangular apertures.

    Finds the first and second digit of the aperture, scales them, and the outputs the original line with scaled digits. Assumes that rectangles have the following format:

    %ADD14R,0.400000X0.150000*%
    %ADDiR,NXN*%
    """
    comma = rec.search(line)
    x = reX.search(line)
    s = res.search(line)
    l = len(line[comma.start()+1:x.start()])
    d1 = float(line[comma.start()+1:x.start()])*scale  # Scale first digit
    dl1 = l - len(str(int(d1))) - 1 # Adjust format precision by number of leading digits + ','
    d2 = float(line[x.start()+1:s.start()])*scale  # Scale second digit
    dl2 = l - len(str(int(d2))) - 1  # Adjust format precision by number of leading digits + ','
    return line[0:comma.start()+1] + format(d1,f'.{dl1}f') + 'X' + format(d2,f'.{dl2}f') + line[s.start():]

unmodified_lines = 0
total_lines = 0

with open(input_file, 'r') as fi, open(output_file, 'w') as fo:
    for line in fi:
        total_lines += 1
        if reXY.search(line):
            out = scaleLinear(line, scale)
        elif reXYIJ.search(line):
            out = scaleArc(line, scale)
        elif reAC.search(line):
            out = scaleCircle(line, scale)
        elif reAR.search(line):
            out = scaleRectangle(line, scale)
        else:
            unmodified_lines += 1
            out = line

        fo.write(out)

print(f'Scaling complete!\nOutput file: {output_file}\nScaling factor: {scale}\nTotal lines read: {total_lines}\nTotal lines modified: {total_lines-unmodified_lines}')