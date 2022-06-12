import imageio
import truchet

def main():
    how_many_tiles = 10
    of_size = 20
    img = truchet.paint_a_truchet(how_many_tiles, of_size)
    imageio.imsave("truchet.gif", img)


if __name__ == '__main__':
    main()

