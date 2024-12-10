# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0


import subprocess
import os


def test_utils_triggers_validate():

    trigger = "test_trigger"
    trigger_path = os.path.realpath(
        os.path.join("tests", "realm_management", "test_triggers", f"{trigger}.json")
    )

    arg_list = [
        "astartectl",
        "utils",
        "triggers",
        "validate",
        trigger_path,
    ]
    trigger_result = subprocess.run(arg_list, capture_output=True, text=True)

    assert trigger_result.returncode == 0
