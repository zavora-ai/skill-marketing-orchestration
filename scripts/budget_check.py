#!/usr/bin/env python3
"""Check if campaign budget is within limits."""
import json, sys

def check(data):
    allocated = data.get("allocated", 0)
    spent = data.get("spent", 0)
    requested = data.get("requested", 0)
    remaining = allocated - spent
    can_launch = requested <= remaining
    return {"can_launch": can_launch, "remaining": remaining, "requested": requested,
            "warning": f"Over budget by ${requested - remaining}" if not can_launch else None}

if __name__ == "__main__":
    print(json.dumps(check(json.loads(sys.argv[1])), indent=2))
