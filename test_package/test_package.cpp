#include <iostream>
#include "lemon/list_graph.h"

using namespace lemon;
using namespace std;
int main()
{
    ListDigraph g;
    ListDigraph::Node u = g.addNode();
    ListDigraph::Node v = g.addNode();
    ListDigraph::Arc a = g.addArc(u, v);
    if (countNodes(g) != 2) return 1;
    if (countArcs(g) != 1) return 1;
    return 0;
}
