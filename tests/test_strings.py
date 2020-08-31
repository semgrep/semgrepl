import semgrepl.main as sm

# Just tests that the function runs
def test_python_function_calls_instance():
    config = sm.init("tests/testcases/python/function_calls/instance.py")
    strings = sm.strings(config)
    assert len(strings) == 13
