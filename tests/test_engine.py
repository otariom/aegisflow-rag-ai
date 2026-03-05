from backend.core.engine import query_engine


def test_query_engine_structure():
    """
    Ensure the query_engine returns the correct response structure.
    """

    question = "What is artificial intelligence?"

    result = query_engine(question)

    assert isinstance(result, dict)

    assert "answer" in result
    assert "sources" in result
    assert "followups" in result


def test_followups_type():
    """
    Ensure followups are returned as a list.
    """

    question = "Explain transparency law."

    result = query_engine(question)

    assert isinstance(result["followups"], list)