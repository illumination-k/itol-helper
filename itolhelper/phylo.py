from Bio.Phylo.BaseTree import Tree, Clade


def attach_id_to_internal_nodes(tree: Tree):
    idx = 0
    for clade in tree.find_clades():
        clade: Clade
        if clade.name is None:
            clade.name = str(idx)
            idx += 1
            
    return tree