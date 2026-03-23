import json

from ll import LinkedList, Node
from playlist import Playlist

with open("songs.json") as f:
    songs = json.load(f)

def load_playlist(ll: LinkedList) -> None:
    for song in songs:
        node = Node(name=song["name"], artist=song["artist"], album=song["album"])
        ll.insert_at_end(node)


def display_playlist(ll: LinkedList) -> None:
    print(f"\nPlaylist ({len(ll)} songs):\n")
    for i, node in enumerate(ll, start=1):
        print(f"  {i}. {node.song_data['name']} — {node.song_data['artist']} ({node.song_data['album']})")


if __name__ == "__main__":
    ll = LinkedList()
    load_playlist(ll)
    display_playlist(ll)

    print("\n--- Testing Playlist Player ---\n")
    player = Playlist(ll)

    player.play()
    player.next()
    player.next()
    player.toggle_shuffle()
    player.next()
    player.next()
    player.toggle_shuffle()
    player.go_to("Bohemian Rhapsody")
    player.previous()
    player.previous()