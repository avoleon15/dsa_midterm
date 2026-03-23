import json

from ll import LinkedList, Node

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
    playlist = LinkedList()
    load_playlist(playlist)
    display_playlist(playlist)
    