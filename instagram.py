'''
Utilizei a lib instapy

na linha 24, você vai passar o caminho de um arquivo que contenha os users que deseja

esse codigo ira interagir com seguidores de determinados usuarios, curtir/comentar/seguir
'''
from instapy import InstaPy
from instapy import smart_run

insta_username = input(str("Username: "))
insta_password = input(str("Password: "))


session = InstaPy(username=insta_username, password=insta_password, headless_browser=False)

with smart_run(session):

    session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers=6700, min_followers=30, min_following=57)


    session.set_action_delays(enabled=True, like=5, comment=10, follow=15)

    usuarios = open("usuarios.txt", "r")
    lista = usuarios.readlines()
    for user in lista:
        session.set_user_interact(amount=2, randomize=True, percentage=40, media=None)
        session.set_do_follow(enabled=False, percentage=10)
        session.set_do_like(enabled=True, percentage=80)
        session.set_do_comment(enabled=False)
        session.interact_user_followers([user], amount=5, randomize=False)
    usuarios.close()
