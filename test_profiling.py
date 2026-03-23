import cProfile
import io
import json
import pstats

from ll import LinkedList, Node
from memory_profiler import profile

with open("songs.json") as f:
    songs = json.load(f)

def load_playlist(ll: LinkedList) -> None:
    for song in songs:
        node = Node(name=song["name"], artist=song["artist"], album=song["album"])
        ll.insert_at_end(node)


@profile
def main():
    playlist = LinkedList()

    profiler = cProfile.Profile()
    profiler.enable()
    load_playlist(playlist)
    profiler.disable()

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).sort_stats("cumulative")
    stats.print_stats(10)
    print(stream.getvalue())

if __name__ == "__main__":
    main()