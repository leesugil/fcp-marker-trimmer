#import xml.etree.ElementTree as ET
from fcp_math import arithmetic
from fcp_io import fcpxml_io

def get_all_markers(clip, tags=['marker', 'chapter-marker', 'keyword']):
    output = []
    for t in tags:
        output += clip.findall(t)
    return output

def trim_markers(clip, fps='100/6000s', debug=False):
    """
    clip: fcpxml clip or asset-clip as an ET element.
    fps: fps of the Project clip (not necessarily the source clip)

    remove all markers, chapter-markers, and keywords placed outside the start and end (start+duration) range.
    helps optimization fcpxml files when there are tons of clip blading on marker-heavy clips

    keep all geq 'start' and less than 'end'
    """
    start = clip.get('start')
    if not start:
        num, denom = arithmetic.unfrac(fps) 
        start = f'0/{denom}s'
    if debug:
        print(f"trim_markers start: {start}, duration: {clip.get('duration')}")
    end = arithmetic.fcpsec_add(a=start, b=clip.get('duration'), fps=fps)

    markers = get_all_markers(clip)
    for m in markers:
        marker_start = m.get('start')
        if arithmetic.fcpsec_gt(start, marker_start) or arithmetic.fcpsec_geq(marker_start, end):
            # marker_start < start, or
            # end <= marker_start
            clip.remove(m)

def trim_markers_in_spine(root, fps='100/6000s', debug=False):
    """
    Assumes the root already has Project and its spine defined in fcpxml
    """
    spine = fcpxml_io.get_spine(root)
    asset_clips = spine.findall('asset-clip')
    
    for c in asset_clips:
        trim_markers(clip=c, fps=fps, debug=debug)
