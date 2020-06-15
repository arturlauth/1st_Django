import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<h1>Video Motivação:</h1>')


def test_home_link(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/429413311"')
