import sys

fn = 'clean_me.png'
from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()


def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled

# def test_PIL():
#     # test PIL
#     print( '\n<< Test of PIL >> \n' )
#     img = Image.open(fn)

#     print(img.format, img.size, img.mode)
#     img.exi
#     info = img._getexif()
#     for k, v in info.items():
#         nice = TAGS.get(k, k)
#         print( '%s (%s) = %s' % (nice, k, v) )

def remove_metadata(filename):
    image = Image.open(filename)
    image_clean = Image.new(image.mode, image.size)
    image_clean.putdata(list(image.getdata()))
    image_clean.save('clean_' + filename)


try:
    exif = get_exif(fn)
    labeled_exif = get_labeled_exif(exif)
    print(labeled_exif)
except:
    print(sys.exc_info()[0])
    print('Error in processing exif data for the specified file')


remove_metadata(fn)