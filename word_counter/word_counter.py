def word_counter():
    text = input("Metni girin: ")
    words = len(text.split())
    characters = len(text)
    print(f"Kelime sayısı: {words}")
    print(f"Karakter sayısı (boşluklarla): {characters}")

word_counter()
