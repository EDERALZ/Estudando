def validate_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, str(cpf)))
    if len(cpf) != 11:
        return False
    if cpf == '00000000000' or cpf == '11111111111' or cpf == '22222222222' or cpf == '33333333333' or cpf == '44444444444' or cpf == '55555555555' or cpf == '66666666666' or cpf == '77777777777' or cpf == '88888888888' or cpf == '99999999999':
        return False
    digits = cpf[:-2]
    checker = cpf[-2:]
    first_verifier = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    second_verifier = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    first_sum = sum([int(digits[i]) * first_verifier[i] for i in range(9)]) % 11
    first_digit = 0 if first_sum < 2 else 11 - first_sum
    second_sum = sum([int(digits[i]) * second_verifier[i] for i in range(10)]) % 11
    second_digit = 0 if second_sum < 2 else 11 - second_sum
    return checker == str(first_digit) + str(second_digit)