import semgrepl.main as sm

def test_go_imports_simple():
    config = sm.init("tests/testcases/go/imports/simple.go")
    imports = sm.imports(config)

    # Would be nice to strip quotes here.
    assert '"fmt"' in imports

def test_java_imports_simple():
    config = sm.init("tests/testcases/java/imports/simple.java")
    imports = sm.imports(config)

    # Do we want / can we get the full path java.util.ArrayList?
    assert "ArrayList" in imports

def test_javascripts_import_simple():
    config = sm.init("tests/testcases/javascript/imports/simple.js")
    imports = sm.imports(config)

    assert '"d3"' in imports

def test_python_imports_simple():
    config = sm.init("tests/testcases/python/imports/simple.py")
    imports = sm.imports(config)
    assert "logging" in imports
