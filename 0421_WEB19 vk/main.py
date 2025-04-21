from pprint import pprint

import vk_api
from login_password import LOGIN, PASSWORD


def captha_handler(captha):
    key = input(f'{captha.get_url()}\n'
                f'Введите капчу по ссылке выше:')
    return captha.try_again(key)


def main():
    vk_session = vk_api.VkApi(LOGIN, PASSWORD,
                              captcha_handler=captha_handler)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as err_msg:
        print(err_msg)
        return

    vk = vk_session.get_api()
    response = vk.wall.get(count=5, offset=1)

    if response['items']:
        for i in response['items']:
            pprint(i)

if __name__ == '__main__':
    main()
