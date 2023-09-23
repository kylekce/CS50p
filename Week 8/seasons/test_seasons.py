import pytest
from seasons import print_seasons

def test_seasons():
    with pytest.raises(SystemExit):
        print_seasons("January 1, 2023")
        print_seasons("Jan 1, 2023")
        print_seasons("01/01/23")
