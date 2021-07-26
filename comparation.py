import torch
from facenet_pytorch import MTCNN
from facenet_pytorch import InceptionResnetV1
from scipy.spatial.distance import euclidean

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

# Function that recognizes faces
facial = MTCNN(
    keep_all=True,
    min_face_size=20,
    thresholds=[0.6, 0.7, 0.7],
    post_process=False,
    image_size=160,
    device=device
)


def comparation(user_pic, user_id):
    # Function that compares the ID image with the capture
    # Returns True if they correspond to the same person, False if they do not correspond

    # Face recognition
    user_pic = facial.forward(user_pic)
    user_id = facial.forward(user_id)

    # Model for converting images into numerical values (embedding)
    encoder = InceptionResnetV1(pretrained='vggface2', classify=False, device=device).eval()

    user_pic_num = encoder.forward(user_pic).detach().cpu()
    user_id_num = encoder.forward(user_id).detach().cpu()

    # Euclidean distance between the face embeddings
    euclidean_dist = euclidean(user_pic_num, user_id_num)
    print(euclidean_dist)
    # Checking if they are likely enough 
    if euclidean_dist > 0.3:
        return False, euclidean_dist
    else:
        return True, euclidean_dist
