import h5py
import cv2
import argparse
import os


def get_name(index, hdf5_data):
    name_ref = hdf5_data['/digitStruct/name'][index].item()
    return ''.join([chr(v[0]) for v in hdf5_data[name_ref]])


def get_bbox(index, hdf5_data):
    attrs = {}
    item_ref = hdf5_data['/digitStruct/bbox'][index].item()
    for key in ['label', 'left', 'top', 'width', 'height']:
        attr = hdf5_data[item_ref][key]
        values = [hdf5_data[attr[i].item()][0][0].astype(int)
                  for i in range(len(attr))] if len(attr) > 1 else [attr[0][0]]
        attrs[key] = values
    return attrs


def convert(directory):
    if not(os.path.exists(f'{directory}/labels/') and os.path.isdir(f'{directory}/labels/')):
        os.makedirs(f'{directory}/labels/')

    with h5py.File(f'{directory}/images/digitStruct.mat') as hdf5_data:
        num_images = len(hdf5_data['/digitStruct/name'])
        print("Number of images: ", num_images)

        for i in range(num_images):
            img_name = get_name(i, hdf5_data)
            print(img_name)
            im = cv2.imread(f'{directory}/images/' + img_name)
            h, w, c = im.shape
            arr = get_bbox(i, hdf5_data)

            with open(f'{directory}/labels/' +
                      img_name.replace('.png', '.txt'), 'w') as fp:
                arr_l = len(arr['label'])
                for idx in range(arr_l):
                    label = arr['label'][idx]
                    if label == 10:
                        label = 0
                    _l = arr['left'][idx]
                    _t = arr['top'][idx]
                    _w = arr['width'][idx]
                    if (_l+_w) > w:
                        _w = w-_l-1
                    _h = arr['height'][idx]
                    if (_t+_h) > h:
                        _h = h-_t-1

                    x_center = (_l + _w/2)/w
                    y_center = (_t + _h/2)/h
                    bbox_width = _w/w
                    bbox_height = _h/h

                    s = str(label)+' '+str(x_center)+' '+str(y_center) + \
                        ' '+str(bbox_width)+' '+str(bbox_height)
                    if idx != (arr_l-1):
                        s += '\n'
                    fp.write(s)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert digitStruct.mat to labels')
    parser.add_argument('-d', '--directory', type=str, required=True, help='Path to the working directory')

    args = parser.parse_args()
    convert(args.directory)
