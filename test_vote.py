import pytest

from vote import vote


@pytest.mark.parametrize(
    "votes, expected",
    [
        (
            [3, 2, 3, 2, 1, 1, 1, 3, 1, 1],
            1
        ),
        (
            [1, 1, 2, 1, 2, 1, 3, 3, 3, 3, 2, 1, 2, 1, 1],
            1
        ),
        (
            [1, 2, 2, 3, 2, 1, 1, 3, 2, 3, 2, 2, 3, 3, 1, 2, 1, 3, 3, 1],
            "Нужен второй тур выборов"
        ),
        (
            [2, 2, 1, 3, 3, 2, 3, 1, 1, 2, 1, 2, 1, 2, 2],
            2
        ),
    ]
)
def test_vote(votes, expected):
    assert vote(votes) == expected