class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        self.delimiter = "/0x$*"

        return self.delimiter.join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        return s.split(self.delimiter)
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

'''
my first thought was to concatenate all the list of strings with an obscure character to mark the separation in between strings,
but the strings it self can contain this delimiter
    maybe a combination of obscure characters like /0x$*

'''