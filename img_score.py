import imquality.brisque as brisque
import PIL.Image
import os


def calculate_scores(arg):
    """
    Calculeaza scorul calitatii imaginilor aflate la path-urile primite
    :param arg: poate sa fie, fie o lista de path-uri de imagini, fie un director ce contine imaginile
    :return: Nothing, just prints the scores
    """

    list_of_scores = []

    if isinstance(arg, list):
        images_path = arg

        for image_path in images_path:
            print("Processing image {} ...".format(image_path))

            img = PIL.Image.open(image_path)
            img_score = int(brisque.score(img))

            list_of_scores.append(img_score)

    elif os.path.isdir(arg):
        images_path = os.listdir(arg)

        list_of_scores = []

        for image_path in images_path:

            image_path = os.path.join(arg, image_path)

            print("Processing image {} ...".format(image_path))

            img = PIL.Image.open(image_path)
            img_score = int(brisque.score(img))

            list_of_scores.append(img_score)

    elif os.path.isfile(arg):
        img = PIL.Image.open(arg)
        img_score = int(brisque.score(img))

        list_of_scores = [img_score]
    else:
        raise Exception("Argumentul nu este nici lista, nici path de imagine, nici director!")

    return list_of_scores, sum(list_of_scores) / len(list_of_scores)


# usecase 1  functia primeste o lista de path-uri catre imagini
# dict_scores_1 = calculate_scores(["C:\\Users\\Desktop\\anaaremere.jpg", "andreea.png", "alexandra.jpg"])

# usecase 2  functia primeste un nume de folder care contine path-uri de imagini
list_of_scores, avg_score = calculate_scores("100 de imagini de testat")
print(list_of_scores)
print(avg_score)
# usecase 3
# tupla = calculate_scores("andreea.png")
