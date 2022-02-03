msg_ = {
    0: "Enter an equation\n", 1: "Do you even know what numbers are? Stay focused!", 2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    3: "Yeah... division by zero. Smart move...", 4: "Do you want to store the result? (y / n):\n", 5: "Do you want to continue calculations? (y / n):\n",
    6: " ... lazy", 7: " ... very lazy", 8: " ... very, very lazy", 9: "You are", 10: "Are you sure? It is only one digit! (y / n)\n",
    11: "Don't be silly! It's just one number! Add to the memory? (y / n)\n", 12: "Last chance! Do you really want to embarrass yourself? (y / n)\n"
}

memory = 0.0

operations_dict = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


def input_answer(msg: str) -> bool:
    answer = None
    while answer not in ('y', 'n'):
        answer = input(msg)
    return True if answer == 'y' else False


def print_comment(x: float, y: float, oper: str) -> None:
    msg = ''

    msg = msg + msg_[6] if (is_one_digit(x) and is_one_digit(y)) else msg
    msg = msg + msg_[7] if (x == 1 or y == 1) and oper == '*' else msg
    msg = msg + msg_[8] if (x == 0 or y == 0) and oper != '/' else msg

    if len(msg):
        print(msg_[9] + msg)


def is_one_digit(val: float) -> bool:
    return True if (-10 < val < 10) and val.is_integer() else False


def confirm_storage(result: float) -> bool:
    msgs = (msg_[10], msg_[11], msg_[12])
    i = 0
    bool_result = input_answer(msg_[4])

    if is_one_digit(result):
        while bool_result and i < len(msgs):
            bool_result = input_answer(msgs[i])
            i += 1

    return bool_result


while True:
    calc = input(msg_[0])
    x_str, oper, y_str = calc.split(' ')

    try:
        x = memory if x_str == 'M' else float(x_str)
        y = memory if y_str == 'M' else float(y_str)

        calc_fn = operations_dict[oper]

        print_comment(x, y, oper)

        result = calc_fn(x, y)
        print(result)

        is_stored = confirm_storage(result)
        memory = result if is_stored else memory

        is_continued = input_answer(msg_[5])
        if not is_continued:
            break

    except ValueError:
        print(msg_[1])
    except KeyError:
        print(msg_[2])
    except ZeroDivisionError:
        print(msg_[3])
