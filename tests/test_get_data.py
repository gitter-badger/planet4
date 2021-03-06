from planet4 import p4io
import datetime as dt


def test_get_numbers_from_date_from_fname():
    fname1 = '/a/b/c/2014-06-02_some_name.h5'
    assert p4io.split_date_from_fname(fname1) == [2014, 6, 2]


def test_get_datetime_object_from_fname():
    fname1 = '/a/b/c/2014-06-02_some_name.h5'
    dt_obj = dt.datetime(2014, 6, 2)
    assert dt_obj == p4io.get_dt_from_fname(fname1)


def test_from_2_files_get_latest_file(monkeypatch):
    import glob
    fname1 = '/a/b/c/2014-06-02_some_name.h5'
    fname2 = '/a/b/c/2014-06-09_some_name.h5'

    def mockreturn(path):
        return [fname1, fname2]

    monkeypatch.setattr(glob, 'glob', mockreturn)
    x = p4io.get_current_database_fname()
    assert x == fname2
