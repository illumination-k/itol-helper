from Bio.Phylo.BaseTree import Clade, Tree  # type: ignore
from pydantic.color import Color
from .datasets.config import ColorMap, EvolutionaryOrderMap


def attach_id_to_internal_nodes(tree: Tree):
    idx = 0
    for clade in tree.find_clades():
        clade: Clade  # type: ignore
        if clade.name is None:
            clade.name = str(idx)
            idx += 1

    return tree


def get_nearest_terminal(clade: Clade) -> str:
    return clade.get_terminals()[0]


def get_minimam_evolutionary_order_name(clade: Clade, evolutionary_order_map: EvolutionaryOrderMap) -> str:
    import heapq
    terminals: list[tuple[int, str]] = []
    heapq.heapify(terminals)
    
    for terminal in clade.get_terminals():
        name = terminal.name
        
        ord = evolutionary_order_map.get_order(name)
        heapq.heappush(terminals, (ord, name))
    
    return heapq.heappop(terminals)[1]


def get_minimum_evolutionary_order_color(clade: Clade, evolutionary_order_map: EvolutionaryOrderMap, colormap: ColorMap) -> str:
    name = get_minimam_evolutionary_order_name(clade, evolutionary_order_map)
    
    return colormap.get_color(name)
