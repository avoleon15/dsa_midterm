import random

from ll import LinkedList, Node


class Playlist:

    def __init__(self, linked_list: LinkedList):
        self.playlist = linked_list
        self.current: "Node | None" = linked_list.start
        self.is_playing: bool = False
        self._shuffle_on: bool = False
        self._shuffle_queue: list[Node] = []
        self._shuffle_index: int = 0

    def play(self) -> None:
        if self.current is None:
            print("No hay canciones en la playlist.")
            return
        self.is_playing = True
        print(f"▶  Reproduciendo: {self.current}")

    def next(self) -> None:
        if self.current is None:
            return

        if self._shuffle_on:
            self._shuffle_index += 1
            if self._shuffle_index >= len(self._shuffle_queue):
                print("⏭  Fin de la playlist en modo shuffle.")
                self._shuffle_index = len(self._shuffle_queue) - 1
                return
            self.current = self._shuffle_queue[self._shuffle_index]
        else:
            if self.current.next is None:
                print("⏭  Ya estás en la última canción.")
                return
            self.current = self.current.next

        self.play()

    def previous(self) -> None:
        if self.current is None:
            return

        if self._shuffle_on:
            self._shuffle_index -= 1
            if self._shuffle_index < 0:
                print("⏮  Ya estás en la primera canción del shuffle.")
                self._shuffle_index = 0
                return
            self.current = self._shuffle_queue[self._shuffle_index]
        else:
            if self.current.prev is None:
                print("⏮  Ya estás en la primera canción.")
                return
            self.current = self.current.prev

        self.play()

    def toggle_shuffle(self) -> None:
        self._shuffle_on = not self._shuffle_on

        if self._shuffle_on:
            remaining = []
            node = self.current.next if self.current else self.playlist.start

            while node is not None:
                remaining.append(node)
                node = node.next

            random.shuffle(remaining)
            self._shuffle_queue = (
                [self.current] + remaining if self.current else remaining
            )
            self._shuffle_index = 0
            print("🔀  Shuffle ON")
        else:
            self._shuffle_queue = []
            self._shuffle_index = 0
            print("🔀  Shuffle OFF — retomando orden original")

    def go_to(self, song_name: str) -> None:
        node = self.playlist.search(song_name)

        if node is None:
            print(f"'{song_name}' no encontrada.")
            return

        self.current = node

        if self._shuffle_on:
            if node in self._shuffle_queue:
                self._shuffle_index = self._shuffle_queue.index(node)
            else:
                self._shuffle_queue.insert(self._shuffle_index + 1, node)
                self._shuffle_index += 1

        self.play()