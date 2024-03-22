from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, filename='app.log',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')


@app.route('/post', methods=['POST'])
def main():
    logging.info('Request: %r', request.json)
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    logging.info('Request: %r', response)
    return jsonify(response)


def handle_dialog(res, req):
    res['response']['buttons'] = get_suggest()

    if req['session']['new']:
        res['response']['text'] = \
            'Сейчас будем смеяться над кониной'
        return

    text = req['request']['original_utterance']
    if 'помощь' in text.lower():
        res['response'][
            'text'] = 'Вы можете отправить текст, нажав на кнопку, и получите ответ. ' \
                      'Чтобы закончить общение, нажмите на кнопку "Закончить"'
        return

    if 'что ты умеешь' in text.lower():
        res['response'][
            'text'] = 'Я умею отвечать на фразы, предложенные на кнопках'
        return

    if 'закончить' in text.lower():
        res['response']['text'] = 'До скорых встреч!'
        res['response']['end_session'] = True
        return

    if 'Иван Жарков проиграл деньги'.lower() in text.lower():
        res['response']['text'] = 'Иван Жарков должен деньги за проигрыш в картах, не повезло ему, хахаха'
        return

    if 'Иван Жарков получил двойку'.lower() in text.lower():
        res['response']['text'] = 'ахахахахахахах, Иван Жарков получил двойку по русскому'
        return

    if 'Иван Жарков проспорил 100 рублей'.lower() in text.lower():
        res['response']['text'] = 'хахахаха, конина проспорила 100 рублей, Может быть, он мне тоже проспорит?'
        return

    if 'Иван Жарков был обрызган'.lower() in text.lower():
        res['response']['text'] = 'хахахаха, Ивана Жаркова обрызгала машина водой из лужи!'
        return

    if 'Ивану Жаркову повезло'.lower() in text.lower():
        res['response']['text'] = 'опа, конине впервые повезло!!!'
        return

    else:
        res['response']['text'] = 'Иван Жарков не понял сообщения'


def get_suggest():
    return [{
        'title': 'Помощь',
        'hide': True
    },
        {
            'title': 'Закончить',
            'hide': True
        },
        {
            'title': 'Что ты умеешь?',
            'hide': True
        },
        {
            'title': 'Иван Жарков проиграл деньги',
            'hide': True
        },
        {
            'title': 'Иван Жарков получил двойку',
            'hide': True
        },
        {
            'title': 'Иван Жарков проспорил 100 рублей',
            'hide': True
        },
        {
            'title': 'Иван Жарков был обрызган',
            'hide': True
        },
        {
            'title': 'Ивану Жаркову повезло',
            'hide': True
        }

    ]


if __name__ == "__main__":
    app.run()
