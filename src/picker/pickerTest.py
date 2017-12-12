from drawing import Drawing
from factory import PickerFactory
from randomPicker import RandomPicker


if __name__ == "__main__":
    d = {"picksPerDrawing": 5, "altReds": False}

    # Test creating pickers


    # Test factory
    pf = PickerFactory()
    print(pf)
    rp = pf.CreatePicker("RandomPicker", **d)
    print(rp)
    rp.Pick(None)
    for draw in rp.GetPicks():
        print(draw)