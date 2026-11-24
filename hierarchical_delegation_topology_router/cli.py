"""CLI for Delegation Topology Router."""
import argparse
from .core import TopologyRouter, DelegationNode

def main():
    parser = argparse.ArgumentParser(description="Hierarchical Delegation Topology Router CLI")
    parser.add_argument("--demo", action="store_true", help="Run topology delegation demo")
    args = parser.parse_args()

    root = DelegationNode("commander", "orchestrator", ["plan"])
    lead = DelegationNode("lead_coder", "manager", ["code_review"])
    worker = DelegationNode("frontend_dev", "specialist", ["react", "typescript"])
    root.add_child(lead)
    lead.add_child(worker)

    router = TopologyRouter(root)
    assigned = router.route_task("react", {"task": "Build button"})
    print(f"Task successfully routed to specialist: {assigned}")

if __name__ == "__main__":
    main()
