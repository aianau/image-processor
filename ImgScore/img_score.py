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

        dict_img_scores = {}

        for image_path in images_path:
            print("Processing image {} ...".format(image_path))

            img = PIL.Image.open(image_path)
            img_score = int(brisque.score(img))

            if img_score > 40:
                dict_img_scores[image_path] = (False, "Calitatea imaginii {} are scorul {} ceea ce inseamna o calitate proasta!".format(image_path, img_score))
            else:
                dict_img_scores[image_path] = (True, "Calitatea imaginii {} are scorul {} ceea ce inseamna o calitate buna!".format(image_path, img_score))

        return dict_img_scores

    elif os.path.isdir(arg):
        images_path = os.listdir(arg)

        dict_img_scores = {}

        for image_path in images_path:

            image_path = os.path.join(arg, image_path)

            print("Processing image {} ...".format(image_path))

            img = PIL.Image.open(image_path)
            img_score = int(brisque.score(img))

            if img_score > 40:
                dict_img_scores[image_path] = (False, "Calitatea imaginii {} are scorul {} ceea ce inseamna o calitate proasta!".format(image_path, img_score))
            else:
                dict_img_scores[image_path] = (True, "Calitatea imaginii {} are scorul {} ceea ce inseamna o calitate buna!".format(image_path, img_score))

        return dict_img_scores

    elif os.path.isfile(arg):
        img = PIL.Image.open(arg)
        img_score = int(brisque.score(img))

        if img_score > 40:
            return (False, "Calitatea imaginii {} are scorul {} ceea ce inseamna o calitate proasta!".format(arg, img_score))
        else:
            return (True, "Calitatea imaginii {} are scorul {} ceea ce inseamna o calitate buna!".format(arg, img_score))
    else:
        raise Exception("Argumentul nu este nici lista, nici path de imagine, nici director!")


if __name__ == '__main__':
    dict_scores_2 = calculate_scores("images")
    print(dict_scores_2)
