def dibujo_ahorcado(hints):
    match hints:
        case 0:
            return
        case 1:
            print("""





                            _______
                    """)
        case 2:
            print("""

                                   |
                                   |
                                   |
                                   |
                            _______|
                    """)
        case 3:
            print("""
                                ---
                                   |
                                   |
                                   |
                                   |
                            _______|
                    """)
        case 4:
            print("""
                                ---
                               |   |
                                   |
                                   |
                                   |
                            _______|
                    """)
        case 5:
            print("""
                                ---
                               |   |
                              _0/  |
                                   |
                                   |
                            _______|
                    """)
        case 6:
            print("""
                                ---
                               |   |
                              _0/  |
                               |   |
                              / \\  |
                            _______|
                    """)
