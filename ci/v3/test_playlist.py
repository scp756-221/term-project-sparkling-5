"""
Test the *_original_artist routines.

These tests are invoked by running `pytest` with the
appropriate options and environment variables, as
defined in `conftest.py`.
"""

# Standard libraries

# Installed packages
import pytest

# Local modules
import playlist


@pytest.fixture
def mserv(request, playlist_url, auth):
    return playlist.Playlist(playlist_url, auth)


@pytest.fixture
def playlist_raw(request):
    content = None
    return content

def get_playlist(playlist):
    return playlist['Items'][0]['music_list']

def test_simple_run(mserv, playlist_raw):
    print("Nothing done here")
    # m_id = mserv.create_playlist(playlist_raw)
    # m_playlist_id = m_id["playlist_id"]

    # playlist_read = mserv.get_playlist(m_playlist_id)
    # cur_playlist = get_playlist(playlist_read)
    # print(cur_playlist)
    # assert 'A' in cur_playlist

    # mserv.add_music(m_playlist_id, 'C')
    # playlist_read = mserv.get_playlist(m_playlist_id)
    # cur_playlist = get_playlist(playlist_read)
    # print(cur_playlist)
    # assert 'C' in cur_playlist

    # mserv.delete_music(m_playlist_id, 'B')
    # playlist_read = mserv.get_playlist(m_playlist_id)
    # cur_playlist = get_playlist(playlist_read)
    # print(cur_playlist)
    # assert 'B' not in cur_playlist

    # mserv.top_music(m_playlist_id, 'C')
    # playlist_read = mserv.get_playlist(m_playlist_id)
    # cur_playlist = get_playlist(playlist_read)
    # print(cur_playlist)
    # assert 'C' == cur_playlist[0]

    # mserv.delete_playlist(m_playlist_id)


# @pytest.fixture
# def song_oa(request):
#     # Recorded 1967
#     return ('Aretha Franklin', 'Respect')


# @pytest.fixture
# def m_id_oa(request, mserv, song_oa):
#     trc, m_id = mserv.create(song_oa[0], song_oa[1])
#     assert trc == 200
#     yield m_id
#     # Cleanup called after the test completes
#     mserv.delete(m_id)


# def test_orig_artist_oa(mserv, m_id_oa):
#     # Original recording, 1965
#     orig_artist = 'Otis Redding'
#     trc = mserv.write_orig_artist(m_id_oa, orig_artist)
#     assert trc == 200
#     trc, oa = mserv.read_orig_artist(m_id_oa)
#     assert trc == 200 and oa == orig_artist


# def test_full_cycle(mserv):
#     # `mserv` is an instance of the `Music` class

#     # Performance at 2010 Vancouver Winter Olympics
#     song = ('k. d. lang', 'Hallelujah')
#     # Soundtrack of first Shrek film (2001)
#     orig_artist = 'Rufus Wainwright'
#     # Original recording from album "Various Positions" (1984)
#     orig_orig_artist = 'Leonard Cohen'

#     # Create a music record and save its id in the variable `m_id`
#     # ... Fill in the test ...
#     trc, m_id = mserv.create(song[0], song[1], orig_artist)
#     assert trc == 200
#     trc, artist, title, oa = mserv.read(m_id)
#     assert (trc == 200 and artist == song[0] and title == song[1]
#             and oa == orig_artist)

#     # Test local adding orig_orig_artist
#     trc, oa = mserv.read_orig_artist(m_id)
#     assert (trc == 200 and oa == orig_artist)
#     trc = mserv.write_orig_artist(m_id, orig_orig_artist)
#     assert trc == 200
#     trc, oa = mserv.read_orig_artist(m_id)
#     assert trc == 200 and oa == orig_orig_artist

#     # The last statement of the test
#     mserv.delete(m_id)
