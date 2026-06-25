from list import list_path

def test_list_path(capsys):
    list_path("../.")

    captured = capsys.readouterr()

    assert ".." in captured.out or "." in captured.out

