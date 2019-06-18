def inputf(text: str) -> float:
    """Simple protected float scanner."""
    try:
        return float(input(text))

    except SystemExit:
        print("\nError: system exit\n")
        exit(-1)

    except KeyboardInterrupt:
        print("\nError: keyboard interrupt\n")
        exit(-1)

    except ValueError:
        print("\nError: invalid values specified")
        exit(-1)

    except TypeError:
        print("\nError: type error")
        exit(-1)
