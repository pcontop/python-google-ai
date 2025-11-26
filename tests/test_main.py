from python_google_ai.main import summarize_text


def test_summarize_text_short():
    assert summarize_text("hello world") == "hello world"


def test_summarize_text_cutoff():
    text = "a" * 200
    assert summarize_text(text, max_len=100) == "a" * 100


def test_summarize_text_none():
    assert summarize_text(None) == ""
