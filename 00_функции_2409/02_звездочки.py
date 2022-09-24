def summary(*nums) -> int:
    """
    Функция будет принимать любое количество аргументов,
    если перед параметром поставить *
    :param nums: число или кортеж чисел,
    :return: результат сложения
    """
    res = 0
    for num in nums:
        res += num
    print(type(nums))
    return res

print(summary(4))
print(summary(4, 6, 7))
print(summary(120, 11, 34, 56, 780, 983, -14, 5))


def contact(**self_fields):
    """
    Параметры с 2 звездочками - это именованные параметры,
    их можно передать в любом количестве.
    :param self_fields:
    :return:
    """
    msg = self_fields
    return msg

print(contact(message='Сайт у вас так себе!',
              phone='+375291234567',
              name='Demid',
              email='example@gmail.com'))
