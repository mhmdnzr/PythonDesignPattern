# for example, we can convert image extension


class ToPngImage:
    def request(self) -> str:
        return "Png"


class JpgImage:
    def specific_request(self) -> str:
        return "Jpg"


class ImageAdapter(ToPngImage, JpgImage):

    def request(self) -> str:
        return f"ImageAdapter: (TRANSLATED) {self.specific_request()}"


def client_code(topngimage: "ToPngImage") -> None:
    print(topngimage.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = ToPngImage()
    client_code(target)
    print("\n")

    ToAdapted = JpgImage()
    print("Client: The ToConvertedImage class has a weird interface. ""See, I don't understand it:")
    print(f"Converted Image: {ToAdapted.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = ImageAdapter()
    client_code(adapter)
