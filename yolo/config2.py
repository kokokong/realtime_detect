import os

#
# path and dataset parameter
#

DATA_PATH = './data'

PASCAL_PATH = os.path.join(DATA_PATH, 'slab')

CACHE_PATH = os.path.join(PASCAL_PATH, 'cache')

OUTPUT_DIR = os.path.join(PASCAL_PATH, 'output')

WEIGHTS_DIR = os.path.join(DATA_PATH, 'weights')

WEIGHTS_FILE = "YOLO_small.ckpt"
# WEIGHTS_FILE = os.path.join(DATA_PATH, 'weights', 'YOLO_small.ckpt')

"""
CLASSES = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus',
           'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant', 'sheep', 'sofa',
           'train', 'tvmonitor']
#"""
"""
CLASSES = ['arles', 'baigneurs', 'deux_danseuses_au_repos', 'en_norvegienne', 'eugene_boch', "femme_a_l'ombrelle_tournee_vers_la_gauche",
        "Homage_to_Cezanne", "jardin_potager_a_L'Hemitage", "la_belle_angele", "la_femme_a_la_cafetiere", "la_fuite_des_nymphes",
        "la_montagne_sainte-victoire", "la_nuit_etoilee", "la_seine_a_vetheuil", "le_pont_boieldieu_a_rouen", "le_talisman",
        "les_glaecons_ou_deebeacle_sur_la", "nature_morte_l'atelier_du_peintre", "rouen_cathedral", "Une_baugnade"]
"""
#"""
CLASSES = ['arles', 'baigneurs', 'deux', 'en_norvegienne', 'eugene_boch', "femme_a_",
        "homage", "jardin", "la_belle", "la_femme", "la_fuite",
        "la_montagne", "la_nuit", "la_seine", "la_pont", "la_talisman",
        "les_glaecons", "l'atelier_du_peintre", "cathedral_monet", "une_baugnade"]
#"""

#CLASSES= ['gundam','driver','gundam','driver','gundam','driver','gundam','driver','gundam','driver','gundam','driver','gundam','driver','gundam','driver','gundam','driver','gundam','driver']
FLIPPED = True


#
# model parameter
#

IMAGE_SIZE = 448

CELL_SIZE = 7

BOXES_PER_CELL = 2

ALPHA = 0.1

DISP_CONSOLE = False

OBJECT_SCALE = 1.0
NOOBJECT_SCALE = 1.0
CLASS_SCALE = 2.0
COORD_SCALE = 5.0


#
# solver parameter
#

GPU = '0'

LEARNING_RATE = 0.0001

DECAY_STEPS = 1000

DECAY_RATE = 0.1

STAIRCASE = True

BATCH_SIZE = 3

MAX_ITER = 15000

SUMMARY_ITER = 10

SAVE_ITER = 3000


#
# test parameter
#

THRESHOLD = 0.2

IOU_THRESHOLD = 0.5
