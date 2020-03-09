def test_title_overline():
    title_string = "==\nAAAAA\n=="
    assert not check_title_overline(title_string=title_string)
