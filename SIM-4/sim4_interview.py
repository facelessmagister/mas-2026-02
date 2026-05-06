#!/usr/bin/env python3
"""
SIM-4 Agent Interview Tool

Load a persona from sim4_personas.json and conduct an interactive interview
with the agent after simulation completion. The agent retains all memories
and final opinion state from the simulation.

Usage:
    python3 sim4_interview.py --agent "Dr Lim Kah Wai"
    python3 sim4_interview.py --agent agent_0006
    python3 sim4_interview.py --list

The agent responds in character using the gpt-oss:120b-cloud model via
the local Ollama gateway.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import textwrap
import urllib.request
from pathlib import Path
from typing import Any, Dict, List

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
MODEL_NAME = "gpt-oss:120b-cloud"
BASE_URL = "http://localhost:11434/v1"
API_KEY = "ollama"
PERSONAS_PATH = Path("/root/projects/mas-2026-02/SIM-4/sim4_personas.json")

# ---------------------------------------------------------------------------
# LLM call
# ---------------------------------------------------------------------------
def llm_chat(messages: List[Dict[str, str]], temperature: float = 0.8, max_tokens: int = 2048) -> str:
    url = f"{BASE_URL}/chat/completions"
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            choice = body["choices"][0]["message"]
            content = choice.get("content") or ""
            if not content.strip():
                content = choice.get("reasoning_content") or choice.get("reasoning") or ""
            return content
    except Exception as exc:
        return f"[Error: {exc}]"

# ---------------------------------------------------------------------------
# Load personas
# ---------------------------------------------------------------------------
def load_personas() -> List[Dict[str, Any]]:
    if not PERSONAS_PATH.exists():
        print(f"Personas file not found at {PERSONAS_PATH}")
        print("Run sim4_engine.py first to generate personas.")
        sys.exit(1)
    return json.loads(PERSONAS_PATH.read_text(encoding="utf-8"))

# ---------------------------------------------------------------------------
# Find agent
# ---------------------------------------------------------------------------
def find_agent(personas: List[Dict[str, Any]], query: str) -> Dict[str, Any] | None:
    for p in personas:
        if p["agent_id"] == query:
            return p
    q = query.lower()
    for p in personas:
        if q in p["name"].lower():
            return p
    return None

# ---------------------------------------------------------------------------
# Interview loop
# ---------------------------------------------------------------------------
def interview_agent(persona: Dict[str, Any]) -> None:
    print(f"\n{'='*70}")
    print(f"  AGENT INTERVIEW: {persona['name']}")
    print(f"  Role: {persona['role']} | Influence: {persona['influence']}/10")
    print(f"  Age: {persona['age']} | Reaction: {persona['reaction_speed']}")
    print(f"{'='*70}\n")

    dim_names = ["Optimism", "Trust in Govt", "Advocacy", "Frustration", "Career Security", "Patient Care Priority"]
    print("Final opinion state from simulation:")
    for idx, dim in enumerate(dim_names):
        val = persona["opinion"][idx]
        bar = "█" * max(0, int(val * 20)) + "░" * max(0, int(-val * 20))
        print(f"  {dim:20s}: {val:+.3f}  {bar}")
    print("")

    memories = persona.get("memories", [])
    if memories:
        print("Recent simulation memories:")
        for m in memories[-5:]:
            print(f"  • {m[:120]}")
        print("")

    print("Type your questions below. 'exit' to quit, 'report' to print current state.\n")

    system_msg = (
        f"You are {persona['name']}, a {persona['role']} in the Malaysian healthcare system. "
        f"Your age is {persona['age']}. Your core stance: {persona['stance']}\n\n"
        "You have just completed a simulation of Malaysia's doctor shortage crisis (2026-2030) under the ENVIRONMENT REFORM policy. "
        "In this scenario, intake stayed flat at 4,820 but working conditions were transformed: permanent posts expanded +10%/year, contract system was abolished, salaries rose 25%, Health Services Commission was established, workload fell to 52 hours/week, and 3-month deployment notice was implemented.\n\n"
        "You retain all memories and opinions from that simulation.\n\n"
        "You are now being interviewed by a researcher about your experiences, perspectives, and recommendations. "
        "Respond authentically as your character. Use Malaysian English / Malay phrases where natural (e.g. 'lah', 'kalau', 'tak boleh tahan'). "
        "Be specific, emotional, and grounded in the simulation events you remember."
    )

    chat_history = [{"role": "system", "content": system_msg}]

    while True:
        try:
            user_input = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting interview.")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit", "q"):
            print("Goodbye.")
            break

        if user_input.lower() == "report":
            print("\n--- Agent State Report ---")
            for idx, dim in enumerate(dim_names):
                print(f"  {dim}: {persona['opinion'][idx]:+.3f}")
            print(f"  Total memories: {len(memories)}")
            print("-" * 40)
            continue

        chat_history.append({"role": "user", "content": user_input})
        raw = llm_chat(chat_history, temperature=0.8, max_tokens=2048)
        chat_history.append({"role": "assistant", "content": raw})

        print(f"\n[{persona['name']}]")
        for line in textwrap.wrap(raw, width=70):
            print(f"  {line}")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Interview SIM-4 agents after simulation.")
    parser.add_argument("--agent", "-a", type=str, help="Agent name or agent_id to interview")
    parser.add_argument("--list", "-l", action="store_true", help="List all available agents")
    args = parser.parse_args()

    personas = load_personas()

    if args.list:
        print(f"\n{'Agent ID':12s} {'Name':30s} {'Role':25s}")
        print("-" * 70)
        for p in personas:
            print(f"{p['agent_id']:12s} {p['name']:30s} {p['role']:25s}")
        print("")
        return

    if not args.agent:
        print("Usage: python3 sim4_interview.py --agent 'Dr Lim Kah Wai'")
        print("       python3 sim4_interview.py --list")
        sys.exit(1)

    agent = find_agent(personas, args.agent)
    if not agent:
        print(f"Agent '{args.agent}' not found. Use --list to see available agents.")
        sys.exit(1)

    interview_agent(agent)

if __name__ == "__main__":
    main()
