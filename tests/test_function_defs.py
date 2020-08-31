import semgrepl.main as sm

def test_python_function_defs_simple():
    config = sm.init("tests/testcases/python/function_defs/simple.py")
    defs = sm.find_all_function_defs(config)
    assert len(defs) == 1
    assert defs[0].name == "foo"

def test_python_function_defs_by_name_simple():
    config = sm.init("tests/testcases/python/function_defs/simple.py")
    defs = sm.find_function_defs_by_name(config, "foo")
    assert len(defs) == 1
    assert defs[0].name == "foo"