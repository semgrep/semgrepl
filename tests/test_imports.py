import semgrepl.main as sm

def test_go_import_simple():
    config = sm.init("tests/testcases/go/imports/simple.go")
    imports = sm.find_imports(config)
    assert '"fmt"' in imports

def test_python_import_simple():
    config = sm.init("tests/testcases/python/imports/simple.py")
    imports = sm.find_imports(config)
    assert "logging" in imports
