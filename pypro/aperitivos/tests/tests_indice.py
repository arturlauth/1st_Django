import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Video Motivação:',
        'Demo Spotify:'
    ]
)
def test_title(resp, titulo):
    assert_contains(resp, titulo)

#
# def test_home_link(resp):
#     assert_contains(resp, '<iframe src="https://player.vimeo.com/video/429413311"')
