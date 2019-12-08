from instapy import InstaPy
from instapy import smart_run

''' Dados do Usuario '''
insta_username = input(str("Username: ")) #Nome do usuario
insta_password = input(str("Password: ")) # Senha do usuario

'''Inicio de sessão no instapy '''
session = InstaPy(username=insta_username, password=insta_password, headless_browser=False)# nome do usuario, senha do usuario, se o navegador vai ser exibido ou rodara em segundo plano


with smart_run(session):

    ''' Definindo requisitos e limites para interagir '''
    session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers=6700, min_followers=30, min_following=57)#numero maximo de seguidores, numero minimo de seguidores, numero minimo de pessoas que a conta segue

    usuarios = open("usuarios.txt", "r")
    lista = usuarios.readlines()
    for user in lista:
        session.set_user_interact(amount=2, randomize=True, percentage=100, media=None)
        session.set_do_follow(enabled=True, percentage=65)
        session.set_do_like(enabled=True, percentage=80)
        session.set_do_comment(enabled=False)
        session.interact_user_followers([user], amount=2, randomize=True)
    usuarios.close()

