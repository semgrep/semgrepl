import semgrepl.main as sm

def test_python_function_calls_simple():
    config = sm.init("tests/testcases/python/function_calls/simple.py")
    calls = sm.all_function_calls(config)
    assert len(calls) == 1
    assert calls[0].name == "bar"
