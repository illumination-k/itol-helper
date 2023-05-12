import argparse
import logging
import sys
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)


def meme_converter(args: argparse.Namespace):
    logger.debug(args)
    
    tree = ET.parse(args.input)
    root = tree.getroot()
    
    for sequence in root.findall(".//sequence"):
        sequence.attrib["name"] = sequence.attrib.pop("id")
    
    if args.keep_motif_sequences is not None:     
        motif_ids = []
        motifs = root.find("motifs")
        for motif in motifs.findall("motif"):
            if motif.get("name") in args.keep_motif_sequences:
                motif_ids.append(motif.get("id"))
            else:
                logger.debug(f"Removing motif {motif.get('name')}")
                motifs.remove(motif)
            
        for scanned_sites in root.iter("scanned_sites"):
            for scanned_site in scanned_sites.findall("scanned_site"):
                if scanned_site.get("motif_id") not in motif_ids:
                    logger.debug(f"Removing scanned site {scanned_site.get('motif')}")
                    scanned_sites.remove(scanned_site)
                
    if args.output is None:
        tree.write(sys.stdout)
    else:
        tree.write(args.output)