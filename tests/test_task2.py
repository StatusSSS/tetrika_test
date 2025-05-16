import pytest
from tetrika_test.task2.solution import collect_beasts

PAGE1 = """
<div class="mw-category">
  <ul>
    <li><a>Альфа</a></li>
    <li><a>Архи</a></li>
  </ul>
  <a href="/next">Следующая страница</a>
</div>
"""

PAGE2 = """
<div class="mw-category">
  <ul>
    <li><a>Бета</a></li>
  </ul>
</div>
"""

class MockResponse:
    def __init__(self, html):
        self.text = html
    def raise_for_status(self):
        pass

class MockSession:
    def __init__(self, pages):
        self.pages = pages
    def get(self, url):
        return MockResponse(self.pages.pop(0))

@pytest.fixture
def patch_session(monkeypatch):
    monkeypatch.setattr(
        'tetrika_test.task2.solution.requests.Session',
        lambda: MockSession([PAGE1, PAGE2])
    )

def test_collect_beasts(patch_session):
    result = collect_beasts()
    assert result['А'] == 2
    assert result['Б'] == 1

    others = [v for k, v in result.items() if k not in ('А', 'Б')]
    assert all(v == 0 for v in others)
