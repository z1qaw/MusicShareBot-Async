from enum import Enum
from typing import Literal, Set


class ApiObjectName(Enum):
    TRACK = 'song'
    TRACKS = 'songs'
    ARTIST = 'artist'
    ARTISTS = 'artists'
    ALBUM = 'album'
    ALBUMS = 'albums'


ApiObjectNamesPluralType = Set[ApiObjectName]


ApiObjectNamesPlural = {
    ApiObjectName.TRACKS,
    ApiObjectName.ALBUMS,
    ApiObjectName.ARTISTS
}
