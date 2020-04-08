import imquality.brisque as brisque
import PIL.Image
import os


def calculate_scores(arg):
    """
    Calculeaza scorul calitatii imaginilor aflate la path-urile primite
    :param arg: poate sa fie, fie o lista de path-uri de imagini, fie un director ce contine imaginile
    :return: Nothing, just prints the scores
    """
    if isinstance(arg, list):
        images_path = arg
    elif os.path.isdir(arg):
        images_path = os.listdir(arg)
    elif os.path.isfile(arg):
        images_path = [arg]
    else:
        raise Exception("Argumentul nu este nici lista, nici path de imagine, nici director!")

    for image_path in images_path:
        img = PIL.Image.open(image_path)
        print("For image {} quality score is: {}".format(image_path, brisque.score(img)))


calculate_scores("images")
