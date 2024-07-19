from k8s_test_harness.util import docker_util, env_util


def _test_sanity(image_version):
    rock = env_util.get_build_meta_info_for_rock_version(
        "cluster-autoscaler", image_version, "amd64"
    )
    image = rock.image

    app_name = "cluster-autoscaler"
    entrypoint = f"/{app_name}"

    # assert we have the expected files
    process = docker_util.run_in_docker(image, [entrypoint, "version"])
    assert app_name in process.stdout and image_version in process.stdout


def test_cluster_autoscaler_1_24_0():
    _test_sanity("1.24.0")


def test_cluster_autoscaler_1_27_2():
    _test_sanity("1.27.2")
