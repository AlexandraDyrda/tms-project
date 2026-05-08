from src.models.task import get_status

def test_get_status():
    assert get_status() == "TODO"