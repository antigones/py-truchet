import imageio
import truchet

def main():
    how_many_tiles = 10
    of_size = 20
    img = truchet.paint_a_truchet(how_many_tiles, of_size, 'simple')
    imageio.imsave("truchet.gif", img)

    of_size = 21
    img = truchet.paint_a_truchet(how_many_tiles, of_size, 'smith')
    imageio.imsave("truchet_smith.gif", img)
    

if __name__ == '__main__':
    main()

