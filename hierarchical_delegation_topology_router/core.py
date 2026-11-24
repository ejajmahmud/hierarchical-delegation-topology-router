"""Core Delegation Topology Router implementation."""
from typing import Dict, List, Any, Optional

class DelegationNode:
    def __init__(self, node_id: str, role: str, capabilities: List[str]):
        self.node_id = node_id
        self.role = role
        self.capabilities = set(capabilities)
        self.children: List[DelegationNode] = []
        self.completed_tasks = 0

    def add_child(self, child: "DelegationNode"):
        self.children.append(child)

class TopologyRouter:
    def __init__(self, root_node: DelegationNode):
        self.root = root_node

    def route_task(self, required_capability: str, task_payload: Dict[str, Any]) -> Optional[str]:
        # Breadth-first search for best matching worker node
        queue = [self.root]
        candidates = []
        while queue:
            curr = queue.pop(0)
            if required_capability in curr.capabilities:
                candidates.append(curr)
            queue.extend(curr.children)

        if not candidates:
            return None

        # Pick candidate with fewest completed tasks (load balancing)
        best = min(candidates, key=lambda n: n.completed_tasks)
        best.completed_tasks += 1
        return best.node_id
