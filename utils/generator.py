from random import Random, sample


def genToken(length=32):
    """
    token生成(默认32位)
    """
    token = ""
    chars = "0123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ-_"
    temp = len(chars) - 1
    for i in range(length):
        token += chars[Random().randint(0, temp)]
    return token


def genRandomCode(lenguth=6):
    """
    验证码生成(默认6位)
    """
    code_list = []
    for i in range(10):  # 0~9
        code_list.append(str(i))
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(97, 123):  # a-z
        code_list.append(chr(i))
    code = sample(code_list, lenguth)  # 随机取指定位数
    code_num = "".join(code)
    return code_num


def genMd5Password(password, salt=None):
    """
    MD5生成（支持加盐）
    """
    from hashlib import md5
    salted_passowrd = f"{password}{salt}"
    return md5(salted_passowrd.encode("utf-8")).hexdigest()