class Node:
    def __init__(self, name: str, artist: str, album: str):
        self.song_data = {
            "name": name,
            "artist": artist,
            "album": album,
        }
        self.next: "Node | None" = None
        self.prev: "Node | None" = None

    def __repr__(self) -> str:
        return f"(NAME: {self.song_data['name']} | ARTIST: {self.song_data['artist']} | ALBUM: {self.song_data['album']})"


class LinkedList:
    def __init__(self):
        self.start: "Node | None" = None

    def __repr__(self) -> str:
        nodes = ["START"] + [node.song_data["name"] for node in self] + ["NIL"]
        return "\n" + " <--> ".join(nodes)

    def __iter__(self):
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def traverse(self) -> None:
        for node in self:
            print(node.song_data["name"])

    def insert_at_beginning(self, element: "Node") -> None:
        element.next = self.start
        if self.start is not None:
            self.start.prev = element
        self.start = element

    def insert_at_end(self, element: "Node") -> None:
        if self.start is None:
            self.start = element
            return

        node = self.start
        while node.next is not None:
            node = node.next
        node.next = element
        element.prev = node

    def insert_after_node(self, element: "Node", node_reference: str) -> None:
        node = self.start
        while node is not None:
            if node.song_data["name"] == node_reference:
                element.next = node.next
                element.prev = node
                if node.next is not None:
                    node.next.prev = element
                node.next = element
                return
            node = node.next

    def delete_node(self, song_name: str) -> None:
        if self.start is None:
            return

        if self.start.song_data["name"] == song_name:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
            return

        node = self.start
        while node.next is not None:
            if node.next.song_data["name"] == song_name:
                if node.next.next is not None:
                    node.next.next.prev = node
                node.next = node.next.next
                return
            node = node.next

    def search(self, song_name: str) -> "Node | None":
        for node in self:
            if node.song_data["name"] == song_name:
                return node
        return None