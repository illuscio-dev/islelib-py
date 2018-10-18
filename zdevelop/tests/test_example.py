def test_example(example_fixture: int) -> None:
    assert example_fixture == 1


def test_example_failure() -> None:
    assert 1 == 2
