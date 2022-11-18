from io import StringIO

from Bio import Phylo
from Bio.Phylo.BaseTree import Tree

from .phylo import attach_id_to_internal_nodes

def test_attach_id_to_internal_node():
    tree: Tree = Phylo.read(StringIO("(A,(B,C),(D,E));"), "newick")
    tree = attach_id_to_internal_nodes(tree)
    
    assert "0" in [c.name for c in tree.get_nonterminals()]
    assert "1" in [c.name for c in tree.get_nonterminals()]
    assert "2" in [c.name for c in tree.get_nonterminals()]