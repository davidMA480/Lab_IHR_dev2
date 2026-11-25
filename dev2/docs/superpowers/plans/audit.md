# Audit - Final Verification (Devoir 2)

## Instructions for the Assistant
Re-read the implemented source files in `code/` and check each point by citing the relevant file(s) and line(s). Do not modify anything without explicit request: immediately report discrepancies.

---

## Code & Architecture Compliance
- [x] Only authorized source files in `code/` have been modified
- [x] Function signatures and docstrings respected (Purpose, Inputs, Outputs)
- [x] Implementation order followed (leaf functions processed and validated first)
- [x] User confirmation: substring/keyword search (e.g., `"oui" in response`), no strict equality comparisons
- [x] TurtleSim control: active loop/timer for continuous re-publishing to counter the 1-second timeout of `cmd_vel`
- [x] TurtleSim movement: separation of linear and angular velocities (no simultaneous arcs risking collisions)
- [x] LLM integration: correct API Ollama calls with error handling and timeouts
- [x] No `print()` debugging, no hardcoded paths, no dead code/comments

---

## Testing & Validation
- [x] All tests in `Devoir2/test` (or `test/`) are green (100% passed)
- [x] **No test files have been modified**

---

## Real Behavior & System Validation (Manual)
- [x] **ROS 2 Launch**: 6 nodes start without errors using `ROS_LOCALHOST_ONLY=1` and defined `ROS_DOMAIN_ID`
- [x] **Voice Chain & LLM**: Voice commands are transcribed and correctly interpreted by Ollama
- [x] **Dialogue / Confirmation**: State machine requests confirmation and accepts natural responses
- [x] **TurtleSim Execution**: The turtle executes the trajectory (move/turn) without premature stopping
- [x] **Robustness**: The system remains stable if the user cancels, hesitates, or speaks an unknown command

## final audit

No issues found in the code files.

No issues found in the code files.

No issues found in the code files.

No issues found in the code files.

No issues found in the code files.
