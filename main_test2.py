from problem2 import p2
import io


def test_problem1(monkeypatch,capsys):  # or use "capfd" for fd-level
    with open('infile2.txt') as fi:
        lines_i = [line for line in fi]
    str_in = "".join(lines_i)
    with open('outfile2.txt') as fo:
        lines_o = [line for line in fo]
    str_out = "".join(lines_o)
    monkeypatch.setattr('sys.stdin', io.StringIO(str_in))
    p2() 
    captured = capsys.readouterr()
    assert captured.out == str_out
