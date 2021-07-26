import torch
from facenet_pytorch import MTCNN
from facenet_pytorch import InceptionResnetV1
from scipy.spatial.distance import euclidean

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

# Función que reconoce las caras
facial = MTCNN(
    keep_all=True,
    min_face_size=20,
    thresholds=[0.6, 0.7, 0.7],
    post_process=False,
    image_size=160,
    device=device
)


def comparation(user_pic, user_id):
    # Función que compara la imagen de la cédula con la foto actual de la persona
    # Retorna un booleano, verdadero si son la misma persona, falso si no

    # Reconocimiento de las caras
    user_pic = facial.forward(user_pic)
    user_id = facial.forward(user_id)

    # Modelo para pasar la información de las caras a valores numéricos (embedding)
    encoder = InceptionResnetV1(pretrained='vggface2', classify=False, device=device).eval()

    user_pic_num = encoder.forward(user_pic).detach().cpu()
    user_id_num = encoder.forward(user_id).detach().cpu()

    # Distancia euclídea entre los embeddings de las caras
    euclidean_dist = euclidean(user_pic_num, user_id_num)
    print(euclidean_dist)
    # Revisando si se paracen lo suficiente o no
    if euclidean_dist > 0.3:
        return False, euclidean_dist
    else:
        return True, euclidean_dist
