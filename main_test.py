from problem1 import main
import io


def test_myoutput(monkeypatch,capsys):  # or use "capfd" for fd-level
    with open('infile.txt') as fi:
        lines_i = [line for line in fi]
    str_in = "".join(lines_i)
    with open('outfile.txt') as fo:
        lines_o = [line for line in fo]
    str_out = "".join(lines_o)
    monkeypatch.setattr('sys.stdin', io.StringIO(str_in))
    main() 
    captured = capsys.readouterr()
    assert captured.out == str_out
