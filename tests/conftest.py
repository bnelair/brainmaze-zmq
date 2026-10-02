import pytest

# Self-contained on purpose: no imports between test modules, so the suite runs the same
# from the repo root, from the family compat job (`pytest --import-mode=importlib`, any
# pytest >= 8.0) and against the installed wheel.
dummy_constant = "This is a constant"


@pytest.fixture()
def constant_dummy_fixture():
    print(f"Running dummy_fixture with {dummy_constant}")
    yield dummy_constant
    print("Tearing down dummy_fixture")


@pytest.fixture()
def string_test_dummy_fixture():
    print("Running string_test_dummy_fixture")
    yield "This is a constant"
    print("Tearing down string_test_dummy_fixture")
