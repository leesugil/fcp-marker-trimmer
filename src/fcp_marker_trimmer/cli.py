#!/usr/bin/env python3

import argparse
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, unquote

from fcp_io import fcpxml_io

def main():

    # Define possible arguments
    parser = argparse.ArgumentParser(description="Removes Markers placed outside asset-clip range for performance optimization on larger Projects.")
    parser.add_argument("fcpxml_filepath", help="Absolute filepath to fcpxml (required)")
    # output
    parser.add_argument("--affix", type=str, default='markers_trimmed_', help="affix to modify the output filename")
    # debug
    parser.add_argument("--debug", type=str, default=0, help="DEBUG output")

    args = parser.parse_args()

    xf = fcpxml_io.clean_filepath(args.fcpxml_filepath)
    vf = fcpxml_io.clean_filepath(fcpxml_io.parse_fcpxml_filepath(xf))
    print(f"fcpxml file: {xf}")
    print(f"video file: {vf}")

    DEBUG = True if (args.debug == 1) else False

    # <fcpxml>
    tree, root = fcpxml_io.get_fcpxml(xf)
    # '100/6000s'
    fps = fcpxml_io.get_fps(root)

    trim_markers_in_spine(root=root, fps=fps, debug=DEBUG):

    fcpxml_io.save_with_affix(tree=tree, src_filepath=xf, affix=args.affix)

if __name__ == "__main__":
    main()
