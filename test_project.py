import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
import ability_to_pass_providers_e1b30 as mod

def test_cli_runs():
    assert mod.cli([]) in (0, 1)
