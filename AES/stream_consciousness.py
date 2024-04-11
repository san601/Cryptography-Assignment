from Crypto.Cipher import AES
from Crypto.Util import Counter
import random
import requests


# from pwn import *

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


def getText():
    lentmp = 0

    arr = set()
    while True:
        text = requests.get('https://aes.cryptohack.org/stream_consciousness/encrypt/').json()['ciphertext']
        arr.add(text)
        leng = len(arr)
        if leng > lentmp:
            print(arr)
            lentmp = leng


# getText()

text = {'533174238d0f489f43bbab2fa0',
        '5d2a623ce478538e02b8b27df6cbbf48356ae7291d27',
        '5e31723ce478578f0fb8fe2ef7c3a6072f66aa6e',
        '482c7479c87842891aa7fe2feac2bf4e2968eb601965d7e11833069248567f5a0f921cb709857b8fdfea35f74b5a2f0c',
        '5d372675cb7869c60bb5ba7dfec2a8073066b428497dd9b8133841db47022b5a05c01dbb1dc12ffd9ad16cfb505c6959d9',
        '582b6a70d478578f0fb8fe29f7c5bf4c677baf211d29ffbf1c7d0dd74854365c07c00ef209cc38b3d4fc6cf044412c4c9622702e90228f1f2ab0daabdfff93a3d771beb5d793fb0235342b319144ee0a1f9a23503274b82fa10d03a422310af8e37cba4b',
        '4b2c7f3cc93700920bb1a77df8c3f148292fb7210067c2f11f3a41d347467f50158903b613c73cfcdbf420b8455a2b0d8c2f3d2ac1',
        '4c217474cc2853c60bb1fe35fedff14a2e7cb4250d29c2f0147d15c0484b3112018e0bf213da7bbedbfb27b8534b6e4397317e6fa927c11f62bcc1f9ceb79ea4df7ebdaed3c7db4d3660',
        '55647574cc344cca439df931f38cbd48346ae7251f6cc4e1053508dc4e02365440880af21ec63eafd4bf38b8525d2348d824312c9568',
        '502b7079817850940cb6bf3ff3d5ee071367a239496dd9f6562941d9474d2812088f18f21edb3ebdc8e16cf14512275ed46638208966c71e2fb8c2e2cae39fbfd539ffe992c7da4778002e20df42fe581b983e503379f12aab5f12a269',
        '482c633cd93d52940ab6b238bfd8b94e2968e7291a29c2f0102941c641477f4201931bf219c835fbceb82efd1146215f96663f3a8a66cd1262b8daf88be599bec664ff',
        '5530267fcc36079243b6bb7debc3a3496760b2344529d4ed057d08c609413e5c40820af213ce35b3c8fd28b6',
        '5836636fde754d8708bdb03abfcdbf436742ae2c0560d8fd0324',
        '4b2b7370c97869c60bb5a838bfceb44b2e6ab1250d29c2f0143341c641432b1229c00cbd0fc53ffcc8fd2dfb59123d589b2e702b9b36db0331f1c1ed8bff83bcdb7bb8a6c6dadd4c67',
        '522b2a3ce47f4c8a43b3b17df6c2f153282f832f0565cfb8103305925d47335e40880aa05ada2faedbf12bf0451221588c',
        '4b2c67688d39008802a7aa24bfdfbc422b63e7340160c5b8013c08dc5d02375304ce',
        '7f367f6cd9375b8d50adeb6aed9fe54a187df4355c3ae9a9440207861e16334f',
        '55636b3cd836488713a4a771bfe5f143227ca2321f6c96f1057141c641477f54019503a65dda7bb1d3f629b411503b59d80f7722de33c10323a1def28bf69abd9263b9a292c0d34f3d6d782dd45beb58179374',
        '55647574cc344cc60fbbad38bfc9a7423576b3280067d1b810330592474d2b1207851bf212c036fcd8f92ff31f',
        '482c636fc878488911a7bb2eb38ca54f2e7ce723087bc4f1103a04920402375d17c026f216c63aa8d2fd6cf548412b419e663921de32c70231f1cdead9e59fb0d572f1ea92c7da4721662a209156f7145a9e33036b31fa33bb0d3eec34791ce6e032b300b8b53c60253c1f3b19b8b21f2831e1c461279a',
        '542b713cdd2a4f9307f4bf33fb8cb946377fbe60016c91f41d7d03d7095537570ec007b75ace3ea8c9b821e1115c21599d67',
        '4b2c67688d39008a0ca0fe32f98ca54f2e61a033497ddef9057d15da4c4c7f41058502b71e892fb39af529b8425d6e409934262a922ac01e31f1cfe5cfb783bfd363a5a6dbddd34034247465d956ed1d5a943f133f7cfd66a64304a5207f14ece571bc0bbafc6e21383d5a6f05b5f7066039e8c27b69fd9a58bc7dc7360857ef2ad05186eebed07aa534a27c0fa995fcccd2e942fa15847c6f015511077b42'}

known_string = b'crypto{'
# b'crypto{'
# b'The ter'
# b'Why do '
# b'What a '
# b"It can'"
# b'And I s'
# b'But I w'
# b'Dress-m'
# b'Dolly w'
# b'Love, p'
# b'As if I'
# b"I'm unh"
# b'How pro'
# b'Would I'
# b'Our? Wh'
# b'I shall'
# b"No, I'l"
# b'What a '
# b'I shall'
# b'Perhaps'
# b'These h'
# b'Three b'

known_string = b'It can\'t '
# b'I shall, '
# b'Would I h'
# b'As if I h'
# b'What a na'
# b'Perhaps h'
# b'Dolly wil'
# b'Love, pro'
# b'Why do th'
# b'crypto{k3'
# b"It can't "
# b'Dress-mak'
# b'These hor'
# b'And I sha'
# b'What a lo'
# b'Three boy'
# b'How proud'
# b'The terri'
# b'But I wil'
# b"I'm unhap"
# b"No, I'll "
# b'I shall l'
# b'Our? Why '

known_string = b'Dress-making '
# b'crypto{k3y57r'
# b'Dolly will th'
# b'Dress-making '
# b'As if I had a'
# b'Would I have '
# b"I shall, I'll"
# b"No, I'll go i"
# b'Love, probabl'
# b"It can't be t"
# b'Three boys ru'
# b'The terrible '
# b'How proud and'
# b'Perhaps he ha'
# b'But I will sh'
# b'What a lot of'
# b'These horses,'
# b'I shall lose '
# b'Why do they g'
# b'What a nasty '
# b"I'm unhappy, "
# b'And I shall i'
# b'Our? Why our?'
# ...
# known_string = b'Love, probably? They don\'t know '
# b"It can't be torn out, but it can"
# b"I'm unhappy, I deserve it, the f"
# b'What a nasty smell this paint ha'
# b'What a lot of things that then s'
# b'Would I have believed then that '
# b'As if I had any wish to be in th'
# b'Why do they go on painting and b'
# b'But I will show him.'
# b'Perhaps he has missed the train '
# b'And I shall ignore it.'
# b"I shall, I'll lose everything if"
# b'These horses, this carriage - ho'
# b"Dolly will think that I'm leavin"
# b"Love, probably? They don't know "
# b'Our? Why our?'
# b'Three boys running, playing at h'
# b'I shall lose everything and not '
# b'crypto{k3y57r34m_r3u53_15_f474l}'
# b'The terrible thing is that the p'
# b"No, I'll go in to Dolly and tell"
# b'Dress-making and Millinery'
# b"How proud and happy he'll be whe"

for i in text:
    i = bytes.fromhex(i)
    tmp = xor(known_string, i, )
    print(tmp.hex())
    for j in text:
        print(xor(tmp, bytes.fromhex(j)))
    print('-----------------')
    input()
