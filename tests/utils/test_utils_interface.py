# SPDX-FileCopyrightText: 2024 SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0


import subprocess
import os


def test_utils_valid_interface_validate():
    interface = "test.astarte-platform.draft.interfaces.Install"

    interface_path = os.path.realpath(
        os.path.join("tests", "realm_management", "test_interfaces", f"{interface}.json")
    )

    arg_list = [
        "astartectl",
        "utils",
        "interfaces",
        "validate",
        interface_path,
    ]

    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)

    assert sample_data_result.returncode == 0


def test_utils_invalid_interface_validate():
    interface = "test.invalid.interface"

    interface_path = os.path.realpath(
        os.path.join("tests", "realm_management", "test_interfaces", f"{interface}.json")
    )

    arg_list = [
        "astartectl",
        "utils",
        "interfaces",
        "validate",
        interface_path,
    ]

    sample_data_result = subprocess.run(arg_list, capture_output=True, text=True)
    expected_result = "is not a valid Astarte Interface"
    assert expected_result in sample_data_result.stderr
