import semgrepl.main as sm

def test_python_import_simple():
    config = sm.init("tests/testcases/python/imports/simple.py")
    imports = sm.find_imports(config)
    assert "logging" in imports
