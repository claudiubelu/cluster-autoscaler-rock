#
# Copyright 2024 Canonical, Ltd.
#

import subprocess

from k8s_test_harness.util import env_util
import pytest


@pytest.mark.parametrize("image_version", ("1.24.0", "1.27.2"))
def test_sanity(image_version):
    rock = env_util.get_build_meta_info_for_rock_version(
        "cluster-autoscaler", image_version, "amd64"
    )
    image = rock.image

    entrypoint = "/cluster-autoscaler"
    # assert we have the expected files
    docker_run = subprocess.run(
        ["docker", "run", "--rm", "--entrypoint", entrypoint, image, "--help"],
        capture_output=True,
        text=True,
    )
    assert "Usage of /cluster-autoscaler:" in docker_run.stderr
