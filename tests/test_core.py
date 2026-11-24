"""Tests for TopologyRouter."""
import unittest
from hierarchical_delegation_topology_router.core import TopologyRouter, DelegationNode

class TestTopologyRouter(unittest.TestCase):
    def test_routing_to_specialist(self):
        root = DelegationNode("root", "admin", [])
        w1 = DelegationNode("w1", "coder", ["python"])
        w2 = DelegationNode("w2", "coder", ["rust"])
        root.add_child(w1)
        root.add_child(w2)

        router = TopologyRouter(root)
        assigned = router.route_task("rust", {"data": "calc"})
        self.assertEqual(assigned, "w2")

    def test_unsupported_capability(self):
        root = DelegationNode("root", "admin", ["bash"])
        router = TopologyRouter(root)
        self.assertIsNone(router.route_task("quantum_computing", {}))
